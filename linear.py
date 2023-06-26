# # import pandas as pd
# # from sklearn.svm import SVR

# # # Read the CSV file
# # data = pd.read_csv('share-of-final-energy-consumption-from-renewable-sources (1).csv')

# # # Filter the data for the year range 2000-2020
# # filtered_data = data[(data['Year'] >= 2000) & (data['Year'] <= 2020)]

# # # Group the data by country
# # grouped_data = filtered_data.groupby('Country')

# # # Create an empty DataFrame to store the predictions
# # predictions = pd.DataFrame(columns=['Country', 'Predicted_2030'])

# # # Iterate over each country group
# # for country, group in grouped_data:
# #     # Prepare the data for SVR
# #     X = group[['Year']]
# #     y = group[['Renewable energy share in the total final energy consumption (%)']]

# #     # Create and fit the SVR model
# #     model = SVR()
# #     model.fit(X, y.values.ravel())

# #     # Predict the renewable energy share for 2030
# #     predicted_2030 = model.predict([[2030]])

# #     # Add the country and prediction to the DataFrame
# #     predictions = predictions.append({'Country': country, 'Predicted_2030': predicted_2030[0]}, ignore_index=True)

# # # Save the predictions to a CSV file
# # predictions.to_csv('predictionsSVR.csv', index=False)