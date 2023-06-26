


import pandas as pd
from sklearn.svm import SVR

# Read the CSV file
data = pd.read_csv('share-of-final-energy-consumption-from-renewable-sources.csv')

# Get the unique countries in the dataset
countries = data['Country'].unique()

# Create an empty DataFrame to store the predictions
predictions = pd.DataFrame(columns=['Country', 'Year', 'Predicted Share'])

# Iterate over each country
for country in countries:
    # Filter the data for the current country
    country_data = data[data['Country'] == country]
    
    # Extract the features (Year) and target variable (Renewable energy share)
    X = country_data[['Year']]
    y = country_data[['Renewable energy share in the total final energy consumption (%)']]
    
    # Create an SVR model
    model = SVR()
    
    # Train the model
    model.fit(X, y)
    
    # Make predictions for each year from 2020 to 2030
    future_years = range(2018, 2031)
    country_predictions = model.predict([[year] for year in future_years])
    
    # Create a DataFrame for the predictions of the current country
    country_results = pd.DataFrame({
        'Country': [country] * len(future_years),
        'Year': future_years,
        'Predicted Share': country_predictions
    })
    
    # Append the country predictions to the overall predictions DataFrame
    predictions = predictions.append(country_results, ignore_index=True)

# Save the predictions to a CSV file
predictions.to_csv('predictions2SVRFrom2018-2030.csv', index=False)




