#!/usr/bin/env bash

BASE_URL="http://localhost:8000";
curl "$BASE_URL/npl?question=Dame+las+ventas+del+producto+K1010148001+en+el+mes+de+enero+de+2020";

echo ""
echo "-----------------------------------------"
echo "           GrapthQL Query"
echo "-----------------------------------------"

curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "query": "{ data(idCliCliente: \"some\") { descGaCategoriaProducto } }" }' \
  $BASE_URL/graphql | jq