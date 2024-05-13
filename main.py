import graphene
import pandas as pd

from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp


class Data(graphene.ObjectType):
    id_tie_fecha_valor = graphene.String()
    id_cli_cliente = graphene.Int()
    id_ga_vista = graphene.Int()
    id_ga_tipo_dispositivo = graphene.Int()
    id_ga_fuente_medio = graphene.Int()
    desc_ga_sku_producto = graphene.String()
    desc_ga_categoria_producto = graphene.String()
    fc_agregado_carrito_cant = graphene.Int()
    fc_ingreso_producto_monto = graphene.Int()
    fc_retirado_carrito_cant = graphene.Int()
    fc_detalle_producto_cant = graphene.Int()
    fc_producto_cant = graphene.Int()
    desc_ga_nombre_producto = graphene.String()
    fc_visualizaciones_pag_cant = graphene.Int()
    flag_pipol = graphene.String()
    sasasa = graphene.String()
    id_ga_producto = graphene.Int()
    desc_ga_nombre_producto_1 = graphene.String()
    desc_ga_sku_producto_1 = graphene.String()
    desc_ga_marca_producto = graphene.String()
    desc_ga_cod_producto = graphene.String()
    desc_categoria_producto = graphene.String()
    desc_categoria_prod_principal = graphene.String()


class Query(graphene.ObjectType):
    data = graphene.List(Data)

    def resolve_data(self, info, fc_ingreso_producto_monto = None):
        df = pd.read_csv('data.csv')
        data = df.to_dict('records')
        fetched_data = [Data(**d) for d in data]
        print(fetched_data)
        return fetched_data

schema = graphene.Schema(query=Query)
app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=schema))

@app.get('/npl')
async def npl_search(question: str):
    """This function resolve the NPL search endpoint funcionalities."""
    return (f'{question}: '
        'Las ventas de la categoría de productos de belleza como el'
        ' K1010148001 en el 2020 son por un total de 70 millones.')