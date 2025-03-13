# Core Proagro Perícia UI

## Sobre a Cresol
A **Cresol** é uma instituição financeira cooperativa que busca fornecer soluções inovadoras para seus associados, garantindo eficiência e segurança em seus serviços.

## Objetivo do Projeto
O **Core Proagro Perícia UI** é um portal destinado aos peritos responsáveis por clientes, permitindo o acesso e gerenciamento de suas respectivas RCPs/declarações.

## Instalação e Configuração

### Pré-requisitos
Certifique-se de ter instalado:
- [Node.js](https://nodejs.org/)
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Extensões recomendadas para VSCode
Para manter a padronização do código, instale as seguintes extensões:
- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Jest](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

### Instalando as dependências do projeto
Execute o seguinte comando na raiz do projeto:

```sh
npm install
```

## Padronização de Código
O projeto segue um padrão de código padronizado utilizando **Prettier** e **ESLint**.

### Configuração de Identação
- **Prettier**: Formatação automática do código.
- **ESLint**: Garantia das boas práticas e padrões definidos no projeto.

## Testes Automatizados
O projeto utiliza **Jest** como ferramenta de controle de qualidade. **Nenhum código pode ser mergeado sem passar nos testes.**

- Todos os componentes devem conter ao menos um teste.
- Caso existam bugs nos testes, o código não poderá ser enviado para PR.

## Padrão de Nomenclatura das Branches
As branches devem seguir o seguinte formato:

```
feature/entregavel/issue/{task}
fix/entregavel/issue/{task}
chore/entregavel/issue/{task}
refactor/entregavel/issue/{task}
```

## Convenção de Código
### Padrão de escrita
- **Arquivos e componentes** → Inglês (`en`)
- **Parâmetros, variáveis e hooks** → Português (`pt-br`)

### Padrão de Nomeação
- O projeto segue a convenção **camelCase**.

---
Seguindo essas diretrizes, garantimos um código padronizado e de fácil manutenção.

Varáveis de acesso (entre em contato com o techlead para obter as credenciais):

```json
KEYCLOAK_CLIENT_ID=
KEYCLOAK_SECRET=
KEYCLOAK_ISSUER=
BASE_URL=
NEXTAUTH_URL=
NEXTAUTH_SECRET=
KEYCLOAK_END_SESSION_URL=
KEYCLOAK_REFRESH_TOKEN_URL=
NEXT_PUBLIC_BASE_URI=
NEXT_PUBLIC_KEY_CRIPTOGRAFIA=
```

## Comandos REGISTRO

Osb: certifique-se de ter a VPN insalada.

```json
npm config set strict-ssl false
```

Crie um arquivo `.npmrc` na raiz do projeto com o seguinte conteúdo:
```json
registry=https://npm.cresolconfederacao.com.br:4873/
```