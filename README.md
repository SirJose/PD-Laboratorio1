
# Descripción
Laboratorio 1 del curso de Product Development. 

## Link [GitHub repo](https://github.com/SirJose/PD-Laboratorio1)

## Ultimo release [v1.0.1](https://github.com/SirJose/PD-Laboratorio1/releases/tag/v1.0.1)

# Pasos
Se deben ejecutar los siguientes comandos en el orden establecido a continuación:

### 1. Instalar dependencias:
```bash
pip install -r requirements.txt
```
### 2. Descarga el dataset: 
```bash
./download_data.sh
```
- *Nota:* no pude hacer que `dvc` funcionara con `google drive`, asi que este comando es una alternativa para obtener el dataset desde mi google drive. En futuras ocasiones usare AWS. En caso de ocurrir algun error, por favor descargar el archivo manualmente (ver links abajo) y guardarlo en esta ubicacion: `data/data.csv`

### 3. Ejectuar el archivo `pipeline.py`:
```bash
py pipeline.py
```

### 

# Dataset utilizado (.csv)
- **Folder:** [Carpeta en Google Drive](https://drive.google.com/drive/folders/13o-r9HxIDKNRz8YQDL4TIc-qfvr1M8lj?usp=sharing)
- **Archivo:** [Archivo CSV en Google Drive](https://drive.google.com/file/d/1dfJnf-r6O0e8zo--BDOmlm5yN_fkumvs/view?usp=drive_link)