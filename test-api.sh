#!/usr/bin/env bash

curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "query": "{ datos(fc_ingreso_producto_monto: \"K1010148001\") { id_tie_fecha_valor id_cli_cliente id_ga_vista id_ga_tipo_dispositivo id_ga_fuente_medio desc_ga_sku_producto desc_ga_categoria_producto fc_agregado_carrito_cant fc_ingreso_producto_monto fc_retirado_carrito_cant fc_detalle_producto_cant fc_producto_cant desc_ga_nombre_producto fc_visualizaciones_pag_cant flag_pipol SASASA id_ga_producto desc_ga_nombre_producto_1 desc_ga_sku_producto_1 desc_ga_marca_producto desc_ga_cod_producto desc_categoria_producto desc_categoria_prod_principal } }" }' \
  http://localhost:8000/graphql