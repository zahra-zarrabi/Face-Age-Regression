{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Inference.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMvFSH5P3mkxVRr7MJDDvPe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zahra-zarrabi/Face-Age-Regression/blob/main/Inference.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cUGTDI32yS7F"
      },
      "outputs": [],
      "source": [
        "import torch\n",
        "import torchvision\n",
        "import argparse\n",
        "from Model import Model\n",
        "import cv2\n",
        "import numpy as np\n",
        "from retinaface import RetinaFace"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "my_parser = argparse.ArgumentParser()\n",
        "my_parser.add_argument('--device',default='cpu', type=str)\n",
        "my_parser.add_argument('--model_path', type=str)\n",
        "my_parser.add_argument('--image_path', type=str)\n",
        "args=my_parser.parse_args()"
      ],
      "metadata": {
        "id": "jLgMUvxIyry0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "transform = torchvision.transforms.Compose([\n",
        "                                            torchvision.transforms.ToPILImage(),\n",
        "                                            torchvision.transforms.ToTensor(),\n",
        "                                            torchvision.transforms.RandomHorizontalFlip(),\n",
        "                                            torchvision.transforms.Normalize((0),(1))\n",
        "])"
      ],
      "metadata": {
        "id": "Gs0a5azK4Ixq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "device = torch.device('cuda' if torch.cuda.is_available() and args.device=='GPU' else 'cpu')\n",
        "model = Model()\n",
        "model = model.to(device)"
      ],
      "metadata": {
        "id": "tiJbM4Hh4sxx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.load_state_dict(torch.load(args.model_path ,map_location=torch.device(args.device)))"
      ],
      "metadata": {
        "id": "YT_hS2-W5gFY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def process_and_predict(image_path):\n",
        "  faces=RetinaFace.extract_faces(img_path=image_path,align=True)\n",
        "  image=faces[0]\n",
        "  image=cv2.resize(image, (width,height))\n",
        "  plt.imshow(image)\n",
        "\n",
        "  tensor = transform(image).unsqueeze(0).to(device)\n",
        "\n",
        "  model.eval()\n",
        "\n",
        "  age=model(tensor)\n",
        "  print(age)\n",
        "\n",
        "  \n",
        "pred = process_and_predict(args.image_path)\n",
        "print('prediction:',pred)"
      ],
      "metadata": {
        "id": "wg1gf7aB5-V2"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}