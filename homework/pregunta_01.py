# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    # Ruta de datos y carpeta de salida
    data_path = "./files/input/shipping-data.csv"
    output_dir = "files/docs"

    # Crear la carpeta `docs` si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Cargar los datos
    def load_data():
        return pd.read_csv(data_path)

    df = load_data()

    # Crear visualización para Warehouse_block
    def create_visual_for_shipping_per_warehouse(df):
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(f"{output_dir}/shipping_per_warehouse.png")
        plt.close()

    # Crear visualización para Mode_of_Shipment
    def create_visual_for_mode_of_shipment(df):
        plt.figure()
        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.savefig(f"{output_dir}/mode_of_shipment.png")
        plt.close()

    # Crear visualización para Customer_rating
    def create_visual_for_customer_rating(df):
        plt.figure()
        counts = df.Customer_rating.value_counts().sort_index()
        counts.plot.bar(
            title="Customer Rating",
            xlabel="Rating",
            ylabel="Count",
            color="tab:green",
            fontsize=8,
        )
        plt.savefig(f"{output_dir}/customer_rating.png")
        plt.close()

    # Crear visualización para Weight_in_gms
    def create_visual_for_weight_in_gms(df):
        plt.figure()
        df.Weight_in_gms.plot.hist(
            bins=20, color="tab:red", title="Weight in gms"
        )
        plt.xlabel("Weight (gms)")
        plt.ylabel("Frequency")
        plt.savefig(f"{output_dir}/weight_in_gms.png")
        plt.close()

    # Llamar a las funciones de visualización
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_customer_rating(df)
    create_visual_for_weight_in_gms(df)

    # Crear el archivo HTML
    html_content = f"""
    <html>
    <head><title>Shipping Dashboard</title></head>
    <body>
        <h1>Shipping Dashboard</h1>
        <h2>Shipping per Warehouse</h2>
        <img src="shipping_per_warehouse.png" width="600">
        <h2>Mode of Shipment</h2>
        <img src="mode_of_shipment.png" width="600">
        <h2>Customer Rating</h2>
        <img src="customer_rating.png" width="600">
        <h2>Weight in gms</h2>
        <img src="weight_in_gms.png" width="600">
    </body>
    </html>
    """

    with open(f"{output_dir}/dashboard.html", "w") as f:
        f.write(html_content)

    print(f"Dashboard generado en la carpeta: {output_dir}")