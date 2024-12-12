# Util_Python_Reader


Este projeto automatiza a geração de um arquivo `.txt` consolidado contendo todos os arquivos Python (`.py`) de um diretório especificado, excluindo os arquivos e diretórios configurados na lista de ignorados.

## Configuração e Uso

### Estrutura
- **Diretório raiz**: Defina o diretório raiz onde os arquivos Python estão localizados.
- **Arquivos ignorados**: Especifique os arquivos Python que não devem ser incluídos na lista `ignore_files_list`.
- **Diretórios ignorados automaticamente**:
  - `.venv`
  - `.idea`
  - `__pycache__`

### Entrada

`project_directory = r"C:\Users\usuario\Desktop\MeuProjeto"
`
`
ignore_files_list = ["main.py", "test.py"]
`


