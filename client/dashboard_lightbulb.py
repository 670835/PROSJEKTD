import tkinter as tk
from tkinter import ttk
import logging
import requests

import common


def lightbulb_cmd(state, did):
    # Konverter valgt radioknapp-verdi til bool
    value = True if state.get() == "On" else False
    logging.info(f"Dashboard: {value}")

    # Korrekt URL til sky-tjenesten
    url = f"{common.BASE_URL}smarthouse/actuator/{did}/"

    try:
        response = requests.put(url, json={"state": value})

        if response.status_code == 200:
            logging.info("Lyspære-status sendt OK")
        else:
            logging.warning(f"Feil ved sending: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"Exception ved sending: {e}")


def init_lightbulb(container, did):
    lb_lf = ttk.LabelFrame(container, text=f'LightBulb [{did}]')
    lb_lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.W)

    # Variabel for lyspærestatus
    lightbulb_state_var = tk.StringVar(None, 'Off')

    on_radio = ttk.Radiobutton(lb_lf, text='On', value='On',
                               variable=lightbulb_state_var,
                               command=lambda: lightbulb_cmd(lightbulb_state_var, did))
    on_radio.grid(column=0, row=0, ipadx=10, ipady=10)

    off_radio = ttk.Radiobutton(lb_lf, text='Off', value='Off',
                                variable=lightbulb_state_var,
                                command=lambda: lightbulb_cmd(lightbulb_state_var, did))
    off_radio.grid(column=1, row=0, ipadx=10, ipady=10)

    off_radio = ttk.Radiobutton(lb_lf, text='Off', value='Off',
                                variable=lightbulb_state_var,
                                command=lambda: lightbulb_cmd(lightbulb_state_var, did))
    off_radio.grid(column=1, row=0, ipadx=10, ipady=10)
