# Código base de la app, sin fórmulas de regresión lineal ni integración de CSV
# Interfaz gráfica con tkinter para consultar el clima de hoy y predicción del clima (molde)

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta

# ---------------------- Configuración ----------------------
COLOR_FONDO = "#f0f4f8"
COLOR_BOTON = "#4CAF50"
COLOR_BOTON_SEC = "#2196F3"
COLOR_TEXTO = "#333333"
FUENTE_TITULO = ("Segoe UI", 16, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)

# Lista de ciudades predeterminadas de México
ciudades_mexico = [
    "Ciudad de México", "Guadalajara", "Monterrey",
    "Puebla", "Cancún", "Mérida", "Tijuana", "León"
]

# Fechas límites para predicción
hoy = datetime.now().date()
min_fecha = hoy + timedelta(days=1)  # desde mañana
max_fecha = datetime(hoy.year + 1, hoy.month, hoy.day).date()  # fin de año actual

# ---------------------- Funciones ----------------------
def abrir_clima_hoy():
    hoy_win = tk.Toplevel(root)
    hoy_win.title("Clima de Hoy")
    hoy_win.geometry("400x220")
    hoy_win.configure(bg=COLOR_FONDO)

    tk.Label(hoy_win, text="Consulta el clima de hoy", font=FUENTE_TITULO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

    tk.Label(hoy_win, text="Selecciona ciudad:", font=FUENTE_TEXTO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()
    
    ciudad_combo = ttk.Combobox(hoy_win, values=ciudades_mexico, font=FUENTE_TEXTO)
    ciudad_combo.pack(pady=5)
    ciudad_combo.current(0)

    def consultar():
        ciudad = ciudad_combo.get()
        messagebox.showinfo("Clima de Hoy", f"Clima de hoy en {ciudad}: Soleado ☀️ (ejemplo)")

    tk.Button(hoy_win, text="Consultar", command=consultar,
              font=FUENTE_TEXTO, bg=COLOR_BOTON_SEC, fg="white",
              relief="flat", padx=10, pady=5).pack(pady=20)


def abrir_prediccion():
    pred_win = tk.Toplevel(root)
    pred_win.title("Predicción del Clima")
    pred_win.geometry("420x320")
    pred_win.configure(bg=COLOR_FONDO)

    tk.Label(pred_win, text="Predicción del clima", font=FUENTE_TITULO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=15)

    tk.Label(pred_win, text="Selecciona ciudad:", font=FUENTE_TEXTO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack()
    
    ciudad_combo = ttk.Combobox(pred_win, values=ciudades_mexico, font=FUENTE_TEXTO)
    ciudad_combo.pack(pady=5)
    ciudad_combo.current(0)

    tk.Label(pred_win, text="Selecciona la fecha:", font=FUENTE_TEXTO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)
    
    fecha_entry = DateEntry(pred_win, width=12, background='darkblue',
                            foreground='white', borderwidth=2,
                            year=min_fecha.year, month=min_fecha.month, day=min_fecha.day,
                            mindate=min_fecha, maxdate=max_fecha,
                            font=FUENTE_TEXTO)
    fecha_entry.pack(pady=5)

    resultado = tk.Label(pred_win, text="", font=FUENTE_TEXTO, bg=COLOR_FONDO)
    resultado.pack(pady=10)

    def predecir():
        ciudad = ciudad_combo.get()
        fecha = fecha_entry.get_date().strftime("%d-%m-%Y")
        resultado.config(text=f"Predicción para {ciudad} el {fecha}: 25.3°C ☀️ (ejemplo)")

    tk.Button(pred_win, text="Predecir", command=predecir,
              font=FUENTE_TEXTO, bg=COLOR_BOTON, fg="white", relief="flat").pack(pady=15)

# ---------------------- Ventana Principal ----------------------
root = tk.Tk()
root.title("App del Clima")
root.geometry("420x280")
root.configure(bg=COLOR_FONDO)

titulo = tk.Label(root, text="☁️ App del Clima ☁️", font=FUENTE_TITULO,
                  bg=COLOR_FONDO, fg=COLOR_TEXTO)
titulo.pack(pady=20)

btn_clima_hoy = tk.Button(root, text="Consultar clima de hoy", command=abrir_clima_hoy,
                          font=FUENTE_TEXTO, bg=COLOR_BOTON_SEC, fg="white",
                          relief="flat", padx=10, pady=5, width=25)
btn_clima_hoy.pack(pady=10)

btn_prediccion = tk.Button(root, text="Predicción del clima", command=abrir_prediccion,
                           font=FUENTE_TEXTO, bg=COLOR_BOTON, fg="white",
                           relief="flat", padx=10, pady=5, width=25)
btn_prediccion.pack(pady=10)

root.mainloop()


