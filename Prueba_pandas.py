import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime
import pandas as pd

# ---------------------- Config ----------------------
COLOR_FONDO = "#f0f4f8"
COLOR_BOTON = "#4CAF50"
COLOR_BOTON_SEC = "#2196F3"
COLOR_TEXTO = "#333333"
FUENTE_TITULO = ("Segoe UI", 16, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)

# ---------------------- Función para procesar temperatura ----------------------
def generar_csv_diario(temp_csv):
    temp_df = pd.read_csv(temp_csv)
    temp_df.columns = temp_df.columns.str.strip()  # limpiar espacios
    temp_df['FechaHora'] = pd.to_datetime(temp_df['FechaHora'])
    temp_df['Temp'] = temp_df['Temp'] - 273.15  # Kelvin → Celsius

    temp_df['Fecha'] = temp_df['FechaHora'].dt.date
    df_diario = temp_df.groupby('Fecha')['Temp'].mean().reset_index()
    return df_diario

# ---------------------- Generar CSV diario ----------------------
df_diario = generar_csv_diario("Temperatura del aire cerca del suelo.csv")

# ---------------------- Función Tkinter ----------------------
def abrir_prediccion():
    pred_win = tk.Toplevel(root)
    pred_win.title("Predicción de Temperatura")
    pred_win.geometry("400x250")
    pred_win.configure(bg=COLOR_FONDO)

    tk.Label(pred_win, text="Predicción de temperatura", font=FUENTE_TITULO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

    tk.Label(pred_win, text="Selecciona la fecha:", font=FUENTE_TEXTO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)
    
    fecha_entry = DateEntry(pred_win, width=12, background='darkblue',
                            foreground='white', borderwidth=2, font=FUENTE_TEXTO)
    fecha_entry.pack(pady=5)

    resultado = tk.Label(pred_win, text="", font=FUENTE_TEXTO, bg=COLOR_FONDO)
    resultado.pack(pady=15)

    def predecir():
        fecha = fecha_entry.get_date()
        fila = df_diario[df_diario['Fecha'] == fecha]
        if not fila.empty:
            fila = fila.iloc[0]
            resultado.config(text=f"Temp promedio el {fecha}: {fila['Temp']:.1f}°C")
        else:
            resultado.config(text="No hay datos para esa fecha.")

    tk.Button(pred_win, text="Mostrar Temperatura", command=predecir,
              font=FUENTE_TEXTO, bg=COLOR_BOTON, fg="white", relief="flat").pack(pady=10)

# ---------------------- Ventana Principal ----------------------
root = tk.Tk()
root.title("App del Clima - AIQ")
root.geometry("400x220")
root.configure(bg=COLOR_FONDO)

tk.Label(root, text="☁️ App del Clima AIQ ☁️", font=FUENTE_TITULO,
         bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)

tk.Button(root, text="Predicción de Temperatura", command=abrir_prediccion,
          font=FUENTE_TEXTO, bg=COLOR_BOTON, fg="white",
          relief="flat", padx=10, pady=5, width=25).pack(pady=20)

root.mainloop()
