try:
    import pandas_datareader.data as web
    print("pandas_datareader found")
except ImportError:
    print("pandas_datareader NOT found")

try:
    import wbdata
    print("wbdata found")
except ImportError:
    print("wbdata NOT found")
