# Docker Image Workflow Practice

This repository contains a simple exercise for practicing fundamental Docker image operations: creating an image, exporting it to a tar archive, and executing it on your local machine.

## 1) Create the image

```bash
docker build -t lab1:v1 .
```

## 2) Export the image to a tar archive

```bash
docker save lab1:v1 > my_image.tar
```

## 3) Execute the image

```bash
docker run lab1:v1
```
