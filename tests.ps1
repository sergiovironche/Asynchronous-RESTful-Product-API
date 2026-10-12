Write-Host "1. Crear Producto 1 (POST)" -ForegroundColor Cyan
curl.exe -X POST "http://127.0.0.1:8000/api/v1/products/" -H "Content-Type: application/json" -d "{\`"sku\`": \`"SKU-001\`", \`"name\`": \`"Teclado\`", \`"price\`": 89.99, \`"stock\`": 50}"
Write-Host "`n"

Write-Host "2. Probar Unicidad de SKU Repetido (POST Error 400)" -ForegroundColor Yellow
curl.exe -X POST "http://127.0.0.1:8000/api/v1/products/" -H "Content-Type: application/json" -d "{\`"sku\`": \`"SKU-001\`", \`"name\`": \`"Otro Teclado\`", \`"price\`": 10.00, \`"stock\`": 5}"
Write-Host "`n"

Write-Host "3. Listar Productos con Pagina y Filtro (GET)" -ForegroundColor Cyan
curl.exe -X GET "http://127.0.0.1:8000/api/v1/products/?skip=0&limit=10&name=Teclado"
Write-Host "`n"

Write-Host "4. Obtener por ID (GET)" -ForegroundColor Cyan
curl.exe -X GET "http://127.0.0.1:8000/api/v1/products/1"
Write-Host "`n"

Write-Host "5. Reemplazo Completo (PUT)" -ForegroundColor Cyan
curl.exe -X PUT "http://127.0.0.1:8000/api/v1/products/1" -H "Content-Type: application/json" -d "{\`"sku\`": \`"SKU-001\`", \`"name\`": \`"Teclado Pro\`", \`"price\`": 119.99, \`"stock\`": 40}"
Write-Host "`n"

Write-Host "6. Actualización Parcial (PATCH)" -ForegroundColor Cyan
curl.exe -X PATCH "http://127.0.0.1:8000/api/v1/products/1" -H "Content-Type: application/json" -d "{\`"stock\`": 35}"
Write-Host "`n"

Write-Host "7. Eliminar Producto (DELETE)" -ForegroundColor Cyan
curl.exe -i -X DELETE "http://127.0.0.1:8000/api/v1/products/1"
Write-Host "`n"