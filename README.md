## Setup

The required Python version is 3.12.3 , and the [Pytorch](https://pytorch.org/) version is 2.3.0.


Additional required packages are listed in the requirements file.
```bash
conda create -n DesignEdit python=3.12.3
conda activate DesignEdit
pip install -r requirements.txt

## Demo
We have created an interactive interface using Gradio, as shown below. You only need to simply run the following command in the environment we previously set up:
```bash
python design_app.py

### 🖱️Usage

- We have 5 function pages for different editing operations.

💡**Object Removal**

💡**Zooming Out**

💡**Camera Panning**

💡**Object Moving, Resizing and Flipping**

💡**Multi-Layered Editing**  



Notice that the **Multi-Layered Editing** page, which uses a multi-layered representation for multiple editing tasks, can achieve the same results as those of Object Removal and Object Moving, Resizing, and Flipping in a general representation.  

Moreover, we have added the "Mask Preparation" page for you to utilize SAM or sketching to combine several masks together. This may be useful when you are on the **Multi-Layered Editing** page.  


