v0.0.1: had a major problem relating to logging but gave functional outputs. Following are the main features of this version:
    1. Fluttershy fetches from CoinGekko, changed in later versions to avoid cache data units in API responses and cause data stagnation in logs
    2. No Pancakes module developed
    3. Main.py runs like a timline, calling different modules for calculations (Fountainin), API fetching (Fluttershy), logging (Engine)
    4. Engine uses csv for logging; first row format: ['index', 'Dime', 'Percentage Change', 'Change in Dime', 'New Dime']
    5. Fountain remains clean and finance relevant for mathematic calculations
    6. Introduced utility-v0.1 inluding temporal-utility, cotaining epoch to imperium and imperium to epoch functions. Not implemented in this version

v0.0.2: Goals:
    1. Plan on developing Pancakes mvp v1: would use PyQt for future proof and learning reasons
    2. Changing API source to other services for real time fluctuation monitoring
    3. Adding timestamps to fluttershy

Chat suggested this for more professionalism, with a mix of more personal fomratting:
# DimeSim Version Control Log

---

## v0.0.1 – Initial Prototype Release
Status: Functional | Logging Bug

Key Features:
1. Fluttershy:
   - Fetches data from CoinGecko API
   - Encountered issues with cached responses causing data stagnation in logs
2. Pancakes:
   - Not developed in this version
3. Main.py:
   - Acts as a timeline-based controller
   - Calls modules for calculations (Fountain), API fetching (Fluttershy), and logging (Engine)
4. Engine Logging:
   - Uses CSV format with the following header:  
     `['index', 'Dime', 'Percentage Change', 'Change in Dime', 'New Dime']`
5. Fountain:
   - Contains mathematically accurate finance-related calculations
6. Utilities (utility-v0.1):
   - Introduced `temporal_utility.py` containing:
     - `epoch_to_imperium()`
     - `imperium_to_epoch()`
   - Not yet implemented

---

## v0.0.2 – Upcoming Goals
Status: In Progress

Planned Features:
1. Pancakes v1 (MVP):
   - Build a basic UI using PyQt for future-proofing and educational purposes
2. API Source Update:
   - Replace CoinGecko with a real-time data service (e.g., Binance or Coinbase)
   - Aims to fix cache-based stagnation
3. Timestamping:
   - Add precise timestamps to Fluttershy logs for better chronological tracking

> Fun Fact: `getResponseJD()` was named after Jason Derulo.  
> Not JSON Data. Not Just Data. Just... Derulo.