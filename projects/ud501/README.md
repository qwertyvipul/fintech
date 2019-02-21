### Slicing the date

Slicing by using Dataframe.ix
```python
print(df.ix[start_date:end_date])
```

Slicing using selected columns
```python
print(df.ix["column"]) # Selecting single column
print(df.ix[["col-1", "col-2"]]) # Selecting multiple column
```

Two dimensional slicing
```python
df2 = df1.ix[start_date:end_date, ["AAPL", "GOOG"]]
```

### Incomplete Data
Avoid peeking into the future

### Histograms

### Portfolio

### Portfolio Statistics
* Cummulative Return
* Avergage Daily Return
* Standard Deviation of Daily Return
* Sharpe Ratio

### Sharpe Ratio
```markdown
sharpe_ratio = mean(daily_return - risk_free_return) / std(daily_return - risk_free_return)
```

### Optimizers

### Porfolio Optimization