Automação de Relatórios 
Este projeto automatiza a geração de documentos (.docx) a partir de templates, otimizando o preenchimento de dados repetitivos e a organização de arquivos.

🚀 Funcionalidades
Geração Automatizada: Cria documentos preenchidos dinamicamente via Python.

Organização de Diretórios: Criação automática de estruturas de pastas para categorização de relatórios.

Padronização: Garante consistência visual e textual em todos os relatórios gerados.

🛠 Tecnologias Utilizadas
Linguagem: Python 3.x

Bibliotecas: python-docx, os, pathlib.

⚙️ Pré-requisitos de Ambiente
Para que este script funcione corretamente, o ambiente de execução deve atender às seguintes condições:

Google Drive for Desktop: O aplicativo deve estar instalado e configurado, permitindo que o script acesse as pastas sincronizadas com a nuvem.

Dependências: Certifique-se de instalar as bibliotecas necessárias:

Bash
pip install python-docx
Configuração de Caminhos: O script utiliza caminhos de diretório locais (configurados no arquivo sistema.py). Ao clonar este repositório, ajuste as variáveis de caminho no código para refletir a estrutura de pastas da sua máquina.

📁 Estrutura do Projeto
sistema.py: Script principal de execução.

interface/: Módulos de interação com o usuário.

arquivo/: Lógica de processamento e manipulação de documentos.

numeros/: Módulos de validação e tratamento de dados.

💡 Observação
Este projeto foi desenvolvido com foco em automação de tarefas repetitivas. A configuração de caminhos absolutos é uma premissa atual do sistema. Futuras atualizações incluirão a refatoração para caminhos relativos, tornando a portabilidade do projeto independente do ambiente.
Além disso, será necessário ajustar os códigos de inserção do Docx de acordo com o template utilizado. 