import pandas as pd
import numpy

'''
 This one is for Popularity Learning
'''

class Popularity_Model():
    # Initialize the variables
	def __init__(self):
		# The training set
		self.train = None

		# User_ID.
		self.Use_ID = None

		# Unique_ISBN of all books
		self.Unique_ISBN = None

		# The final result to be presented. 
		self.Popularity_Model = None
    
    # Initialise the recommendations.
	def initialise(self,train,User_ID,Unique_ISBN):

		# The training data
		self.train = train

		# The id of the user for which the recommendations is needed.
		self.User_ID = User_ID

		# The id of item e.g. Songs, Movies, Products etc.
		self.Unique_ISBN = Unique_ISBN


		# The items are grouped by item_id aggregated with the count of the users and the index is reseted.
		train_grouped = train.groupby([self.Unique_ISBN]).agg({self.User_ID: 'count'}).reset_index()
		# The column named user_id is replaced by the name score.
		train_grouped.rename(columns = {'User_ID': 'Book_Rating'}, inplace = True)


		# The training data is sorted according to the score in descending order and by item_id in ascending order.
		train_sort = train_grouped.sort_values(['Book_Rating', self.Unique_ISBN], ascending = [0,1])

		# The new column named Rank is created by score sorted in ascending order.
		train_sort['Book_Rating'] = train_sort['Book_Rating'].rank(ascending = 0, method = 'first')


		# The first 15 items are saved into the Popularity_Model and it is returned. 
		self.Popularity_Model = train_sort.head(10)
    
	# Method to user created recommendations
	def recommend(self, user_id):

		# Init the user_recommendataion var by popularity_recommendataions since the recommendations has been saved into this column.
		user_recommendataion = self.Popularity_Model

		# Get the user_id
		user_recommendataion['Use_ID'] = user_id

		# Set the columns
		cols = user_recommendataion.columns.tolist()
		cols = cols[-1:] + cols[:-1]
		user_recommendataion = user_recommendataion[cols]

		return user_recommendataion