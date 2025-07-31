import numpy as np
import faiss
import time
import os

# 文件路径设置
data_dir = "/home/faiss/data"
tmpdir = "/tmp/faiss_demo"
os.makedirs(tmpdir, exist_ok=True)

def ivecs_read(fname):
    a = np.fromfile(fname, dtype=np.int32)
    d = a[0]
    return a.reshape(-1, d + 1)[:, 1:].copy()

def fvecs_read(fname):
    return ivecs_read(fname).view(np.float32)

def main():
    start_time = time.time()
    # Stage 0: Train index
    print("Stage 0: Training index")
    xt = fvecs_read(os.path.join(data_dir, "sift_learn.fvecs"))
    d = xt.shape[1]
    index = faiss.index_factory(d, "IVF1024,Flat")
    if xt.shape[0] < 1024 * 39:
       print(f"Warning: {xt.shape[0]} training points, recommended {1024 * 39}")
    index.train(xt)
    faiss.write_index(index, os.path.join(tmpdir, "trained.index"))

    # Stage 1-4: Build block indexes
    xb = fvecs_read(os.path.join(data_dir, "sift_base.fvecs"))
    ntotal = xb.shape[0]
    for bno in range(4):
       print(f"Stage {bno + 1}: Building index for block {bno}")
       i0, i1 = int(bno * ntotal / 4), int((bno + 1) * ntotal / 4)
       index = faiss.read_index(os.path.join(tmpdir, "trained.index"))
       index.add_with_ids(xb[i0:i1], np.arange(i0, i1))
       faiss.write_index(index, os.path.join(tmpdir, f"block_{bno}.index"))

    # Stage 9: Query and merge results
    print("Stage 9: Performing query and merging results")
    xq = fvecs_read(os.path.join(data_dir, "sift_query.fvecs"))
    gt = ivecs_read(os.path.join(data_dir, "sift_groundtruth.ivecs"))
    k = 5
    nprobe = 16

    # 启用 Faiss 多线程加速
    faiss.omp_set_num_threads(4)

    all_D = []
    all_I = []

    for bno in range(4):
       print(f"Searching block {bno}...")
       index = faiss.read_index(os.path.join(tmpdir, f"block_{bno}.index"))
       index.nprobe = nprobe
       D, I = index.search(xq, k)
       all_D.append(D)
       all_I.append(I)

    # Merge results from all blocks
    nq = xq.shape[0]
    merged_D = np.concatenate(all_D, axis=1)  # shape: (nq, 4*k)
    merged_I = np.concatenate(all_I, axis=1)  # shape: (nq, 4*k)

    # Get top-k across all blocks
    final_D = np.zeros((nq, k), dtype=np.float32)
    final_I = np.zeros((nq, k), dtype=np.int64)

    for i in range(nq):
       idx = np.argsort(merged_D[i])[:k]
       final_D[i] = merged_D[i][idx]
       final_I[i] = merged_I[i][idx]

    # Compute recall@1
    recall_at_1 = (final_I[:, :1] == gt[:, :1]).sum() / float(nq)
    print(f"Index size: {ntotal}")
    print(f"Recall@1: {recall_at_1:.3f}")
    print(f"Total time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
