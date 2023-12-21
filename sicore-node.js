const XLSX = require('xlsx');
const fs = require('fs');

// Ruta al archivo Excel que deseas leer
const archivoExcel = 'C:\pruebas-node\pruebas-node.xlsx';

// Lee el archivo Excel
const workbook = XLSX.readFile(archivoExcel);

// Obtiene la primera hoja del archivo Excel
const firstSheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[firstSheetName];

// Convierte la hoja de cálculo en un objeto JSON
const jsonData = XLSX.utils.sheet_to_json(worksheet);

// Imprime los datos en la consola
console.log(jsonData);

// Si quieres imprimir datos específicos, puedes recorrer el JSON
// por ejemplo, para imprimir solo las celdas A1 y B2:
// console.log(jsonData[0]['A1']);
// console.log(jsonData[1]['B2']);
