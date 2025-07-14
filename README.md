# DimeSim 🪙

### 🧪 A Cryptocurrency Market Simulator for Paper-Trading and Behavioral Testing

**DimeSim** is a timeline-driven simulation engine that replicates crypto investing behavior using real market data and virtual capital.  
It’s modular, chaotic, and deeply personal—built to explore how algorithms might perform under historical market conditions.

---

## 🧩 Core Modules

| Module       | Purpose |
|--------------|---------|
| `main.py`    | Timeline orchestrator—calls other modules in sequence |
| `Fountain`   | Pure financial logic (calculations, % change, conversions) |
| `Fluttershy` | API data fetcher (originally CoinGecko) |
| `Engine`     | CSV logger with defined schema |
| `Pancakes`   | *(Upcoming)* Graphical analytics module (planned web-designed MVP) |
| `utility/temporal_utility.py` | Custom time formatting functions (`epoch_to_imperium`, etc.) |

---

## 📦 Current Version: v0.0.1

**Status**: Functional  
**Bug**: Logging was affected by API caching issues

### Highlights:
- CSV-based logging with this format:  
  `['index', 'Dime', 'Percentage Change', 'Change in Dime', 'New Dime']`
- Clean mathematical separation of logic (Fountain) and data (Engine)
- Experimental module names for personality & structure

---

## 📅 Upcoming Goals (v0.0.2)

- ✅ Replace CoinGecko to avoid API caching & stale data
- ✅ Add precise timestamps to log entries via Fluttershy
- 🔄 Begin development of Pancakes:
  - Basic web-based UI for visualizing market performance 
- 🔄 Integrate time utilities (`imperium ↔ epoch`) into log formatting

---

## 🐾 Naming Lore (Because You Know Me)

- **Fluttershy** → fetches fragile API data; often breaks when scared  
- **Fountain** → pure, untouchable logic; calm math zone  
- **Pancakes** → gonna flip your market trends graphically  
- **Engine** → Engine 🧍‍♂️  
- **`getResponseJD()`** → stands for *Jason Derulo*, not JSON Data.  
  Because every call deserves a dramatic entrance.

---

## 📂 Folder Structure (WIP)

```bash
DimeSim/
├── main.py
├── fountain/             # Financial logic
├── fluttershy/           # API handling
├── engine/               # Logging system
├── utility/              # Time + formatting tools
├── pancakes/             # UI layer (WIP)
└── version_control.md    # Devlog & version notes
````

---

## 🤖 Why This Exists

DimeSim was built to test hypothetical crypto investments without using real money.
It’s for:

* Practicing behavioral finance simulation
* Running algorithmic strategy tests
* Having a reason to yell at CSVs at 3AM

---

## 📜 License

MIT – Please use responsibly.
Don’t trust real money with a simulation made by someone who named their logger “Engine.”
