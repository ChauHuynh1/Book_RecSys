# Assignment 2: Group 2 Project: Book Recommender System (Recsys) - Machine Learning (COSC2753)
## Contributors: Nguyen Dang Huynh Chau, Bui Minh Nhat, Tran Phuong Anh


We will discuss:

1. **Data Analysis**
2. **Feature Engineering**
3. **Feature Selection**
4. **Model Training**
5. **Obtaining Predictions / Scoring**

# Data

+ Collected by Cai-Nicolas Ziegler in a 4-week crawl (August / September 2004) from the Book-Crossing community with kind permission from Ron Hornbaker, CTO of Humankind Systems. Contains 278,858 users (anonymized but with demographic information) providing 1,149,780 ratings (explicit / implicit) about 271,379 books. See below for more details. [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)

+ Format:

- The Book-Crossing dataset comprises 3 tables.

***BX-Users***:
Contains the users. Note that user IDs (`User-ID`) have been anonymized and map to integers. Demographic data is provided (`Location`, `Age`) if available. Otherwise, these fields contain NULL-values.

***BX-Books***:
Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (`Book-Title`, `Book-Author`, `Year-Of-Publication`, `Publisher`), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (`Image-URL-S`, `Image-URL-M`, `Image-URL-L`), i.e., small, medium, large. These URLs point to the Amazon web site.

***BX-Book-Ratings***:
Contains the book rating information. Ratings (`Book-Rating`) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.

===========================================================================

# WORKING ON YOUR LOCAL COMPUTER

python version 3.8.8

1. Install Conda
   by [following these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Add Conda
   binaries to your system `PATH`, so you can use the `conda` command on your terminal.

2. Install jupyter lab and jupyter notebook on your terminal

+ `pip install jupyterlab`
+ `pip install jupyter notebook`

### Jupyter Lab

1. Download the 3879312 zipped project folder. Unzip it by double-clicking on it.

2. In the terminal, navigate to the directory containing the project and install these packages and libraries

```
pip install -r requirements.txt
```

3. Enter the newly created directory using `cd directory-name` and start the Jupyter Lab.

```
jupyter lab
```

You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by
visiting http://localhost:8888 on your browser.

4. Click on assignment2.ipynb in the browser tab. This will open up my main file in the Jupyter Lab.

### Note: If the Jupyter Notebook is not responding due to many requests

Error [(The page is not responding)](https://stackoverflow.com/questions/48615535/jupyter-notebook-takes-forever-to-open-and-then-pages-unresponsive-mathjax-i)

I had to restart the notebook; and it did not work. This is because I was printing out too much and the following
scripts resolved the issue by clear out all the output to run through the whole kernal:

1. `conda install -c conda-forge nbstripout` or `pip install nbstripout`

2. `nbstripout filename.ipynb`

## Repository Structure

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── Book_List.cvs       <- Book List.
│   ├── Book_Rating.cvs       <- Book Rating.
│   ├── Book-Users.cvs       <- Book Users.
│   ├── Cleaned_Data         <- data is already cleaned after data cleaning step
│   │   │    
│   │   ├── book_cleaned.csv
│   │   └── book_user_explicite_rating.csv
│   │   └── rating_cleaned.py
│   │   └── user_cleaned.py
│   │
│   ├── Image        <- This folder is is for decoration.
│   │   │    
│   │   ├── 1_jVG54DFcmaWeJPuJxbGH3w.png <- This folder is is for decoration.
│   ├── Book_Recommender_EDA.ipynb      <- This file is for data cleaning and EDA.
│   ├── Book_Recommender_Model.ipynb      <- This file is for model training.
│   ├── Hybrid_final.ipynb     <- This file is for hybrid model training.
│   ├── isbn_dictionary.pickle     <- This file is for cleaning the ISBN.

```
