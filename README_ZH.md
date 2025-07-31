<h1 align="center"> Faiss向量数据库</h1>
<p align="center">
  <a href="README.md"><strong>English</strong></a> | <strong>简体中文</strong>
</p>



## 目录

- [仓库简介](#项目介绍)
- [前置条件](#前置条件)
- [镜像说明](#镜像说明)
- [获取帮助](#获取帮助)
- [如何贡献](#如何贡献)

## 项目介绍

[Faiss](https://github.com/facebookresearch/faiss) 是由Facebook AI Reasearch团队开发的一个用于高效相似性搜索和密集向量聚类的库，能够快速处理大规模数据，并且支持在高维空间中进行向量相似性搜索。本商品基于鲲鹏服务器的Huawei Cloud EulerOS 2.0 64bit系统，提供开箱即用的Faiss。

## 核心特性

- **支持大规模向量分块处理：** 通过将海量向量数据划分为多个独立块（block），分别构建本地索引，有效突破单机内存限制，支持亿级向量的分布式式检索架构
- **高精度近似最近邻搜索：** 基于 IVF（倒排文件）+ Flat 编码的索引结构，在保证高召回率的同时显著提升搜索效率，适用于对精度与性能均有要求的工业级应用
- **灵活的索引训练与持久化：** 提供独立的索引训练与添加数据流程，支持将训练好的索引和分块索引分别保存与加载，便于离线构建、在线服务的分离部署

本项目提供的开源镜像商品 [Faiss向量数据库](https://marketplace.huaweicloud.com/hidden/contents/c989ab37-9b79-40d6-9489-1de3ac8d8fe8#productid=OFFI1146359658505064448) 已预先安装1.11.0版本的Faiss及其相关运行环境，并提供部署模板。快来参照使用指南，轻松开启“开箱即用”的高效体验吧。

> **系统要求如下：**
>
> - CPU: 2vCPUs 或更高
> - RAM: 4GB 或更大
> - Disk: 至少 40GB

## 前置条件

[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## 镜像说明

| 镜像规格                                                     | 特性说明                                                 | 备注 |
| ------------------------------------------------------------ | -------------------------------------------------------- | ---- |
| [Faiss-1.11.0-kunpeng](https://github.com/HuaweiCloudDeveloper/faiss-image/tree/Faiss-1.11.0-kunpeng) | 基于鲲鹏服务器 + Huawei Cloud EulerOS 2.0 64bit 安装部署 |      |

## 获取帮助

- 更多问题可通过 [issue](https://github.com/HuaweiCloudDeveloper/faiss-image/issues) 或 华为云云商店指定商品的服务支持 与我们取得联系
- 其他开源镜像可看 [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos)

## 如何贡献

- Fork 此存储库并提交合并请求
- 基于您的开源镜像信息同步更新 README.md
