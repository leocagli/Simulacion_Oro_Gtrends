
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# -------------------------
# PARTE 1: Simular datos
# -------------------------

np.random.seed(42)
T = 252  # Un año bursátil
dates = pd.date_range(start='2024-07-01', periods=T, freq='B')

# Precio del oro simulado con crecimiento suave
gold_price = 3342.6 * np.exp(np.cumsum(np.random.normal(0, 0.01, T)))

# Interés en Google Trends (simulado entre 20 y 100)
google_trends = np.clip(50 + 15 * np.random.randn(T), 20, 100)

# Construir DataFrame
df = pd.DataFrame({
    'Date': dates,
    'GoldPrice': gold_price,
    'GoogleTrends': google_trends
})
df.set_index('Date', inplace=True)

# -------------------------
# PARTE 2: Regresión de minería de datos
# -------------------------

# Retorno logarítmico
df['return'] = np.log(df['GoldPrice']).diff()
df['return_futuro'] = df['return'].shift(-1)

# Regresión: retorno futuro ~ Google Trends
X = sm.add_constant(df['GoogleTrends'][:-1])
y = df['return_futuro'].dropna()
res = sm.OLS(y, X.loc[y.index]).fit()

# Parámetros del modelo dinámico
base_mu = res.params['const']
alpha = res.params['GoogleTrends']
sigma = df['return'].std() * np.sqrt(252)
dt = 1 / 252
N = 10  # Trayectorias simuladas

# -------------------------
# PARTE 3: Simulación Monte Carlo
# -------------------------

sim = np.zeros((T, N))
sim[0] = df['GoldPrice'].iloc[0]

for t in range(1, T):
    mu_t = base_mu + alpha * (df['GoogleTrends'].iloc[t] / 100)
    Z = np.random.normal(0, 1, N)
    sim[t] = sim[t-1] * np.exp((mu_t - 0.5 * sigma ** 2) * dt + sigma * Z * np.sqrt(dt))

# -------------------------
# PARTE 4: Visualización
# -------------------------

plt.figure(figsize=(12, 6))
for i in range(N):
    plt.plot(df.index, sim[:, i], lw=1.5, alpha=0.8)
plt.title('Simulación Monte Carlo con Drift Dinámico (Google Trends)', fontsize=16)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Precio del Oro ($)', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()
