
<h1 align="center">Faiss vector database</h1>
<p align="center">
    <strong>English</strong> | <a href="README_ZH.md">简体中文</a>
</p>





## Table of Contents

- [Repository Introduction](#project-introduction)
- [Prerequisites](#prerequisites)
- [Image Description](#image-description)
- [Get Help](#get-help)
- [How to Contribute](#how-to-contribute)

## Project Introduction



[Faiss](https://github.com/facebookresearch/faiss) is a library developed by the Facebook AI Search team for efficient similarity search and dense vector clustering, capable of quickly processing large-scale data and supporting vector similarity search in high-dimensional spaces. This product provides an out-of-the-box Faiss based on the Huawei Cloud EulerOS 2.0 64-bit system of Kunpeng servers.

## Core Features

- **Support large-scale vector partitioning processing:** By dividing massive vector data into multiple independent blocks and building local indexes, it effectively breaks through the limitations of single machine memory and supports a distributed retrieval architecture with billions of vectors
- **High precision approximate nearest neighbor search:** Based on the index structure of IVF (inverted file)+Flat encoding, it significantly improves search efficiency while ensuring high recall rate, suitable for industrial applications that require both accuracy and performance
- **Flexible index training and persistence:** Provide independent index training and data addition processes, supporting the separate storage and loading of trained indexes and block indexes, facilitating offline construction and separate deployment of online services

The open-source image product [Faiss vector database](https://marketplace.huaweicloud.com/intl/hidden/contents/e16f63f8-916c-4184-8c2f-d1eed32bb970) provided by this project has pre-installed the the 1.11.0 version of Faiss and its related runtime environment, and provides deployment templates. Come and refer to the usage guide to easily start an efficient "out-of-the-box" experience!

> **System requirements are as follows:**
>
> - CPU: 2vCPUs or higher
> - RAM: 4GB or larger
> - Disk: At least 40GB

## Prerequisites



[Register a Huawei account and activate Huawei Cloud](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## Image Description



| Image Specification                                          | Feature Description                                          | Remarks |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------- |
| [Faiss-1.11.0-kunpeng](https://github.com/HuaweiCloudDeveloper/faiss-image/tree/Faiss-1.11.0-kunpeng) | Installed and deployed based on Kunpeng servers + Huawei Cloud EulerOS 2.0 64-bit |         |

## Get Help

- For more questions, you can contact us through [issues](https://github.com/HuaweiCloudDeveloper/faiss-image/issues) or the service support of the specified product in the Huawei Cloud Marketplace.
- For other open-source images, please refer to [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos).

## How to Contribute

- Fork this repository and submit a merge request.
- Synchronously update README.md based on your open-source image information.
