# 🎬 SimplyTube

**SimplyTube** é um aplicativo desktop simples e intuitivo para baixar vídeos e áudios do YouTube de forma rápida e prática.  
Com uma interface gráfica moderna construída com **CustomTkinter**, o programa permite realizar downloads individuais ou de playlists inteiras em poucos cliques.

---

## 🚀 Funcionalidades

- Download de vídeos do YouTube em formato **MP4 (vídeo)**
- Download de áudios em formato **M4A**
- Suporte a **download de playlists completas**
- Seleção de pasta de destino personalizada
- Barra de progresso em tempo real
- Interface moderna e fácil de usar
- Limpeza de cache para evitar erros comuns
- Opção de abrir a pasta de downloads diretamente pelo app

---

## 🛠 Tecnologias Utilizadas

O projeto foi desenvolvido em Python utilizando as seguintes bibliotecas:

- **Python 3**
- CustomTkinter – Interface gráfica moderna
- PyTubeFix – Download de vídeos do YouTube
- Pillow – Manipulação de imagens
- Tkinter – Componentes nativos do Python

---

## 📥 Requisitos

Antes de executar o SimplyTube, certifique-se de ter o Python instalado em sua máquina.

Instale as dependências necessárias com:

```
pip install customtkinter pytubefix pillow
```

---

## ▶ Como Executar


Método 1: Usando o executável (Recomendado para usuários Windows)
1. Vá até a seção Releases

2. Baixe a versão mais recente do SimplyTube.exe

3. Execute o arquivo diretamente (não requer instalação)


Método 2: Executar a partir do código fonte
1. Clone este repositório:

```
git clone https://github.com/seu-usuario/simplytube.git
```

2. Entre na pasta do projeto:

```
cd simplytube
```

3. Execute o programa:

```
python main.py
```

---

## 🧭 Como Usar

### Download de um único vídeo

1. Abra o SimplyTube  
2. Cole o link do YouTube no campo **YouTube Link**
3. Selecione a pasta onde deseja salvar o arquivo
4. Escolha o formato desejado:
   - MP4 para vídeo
   - M4A para áudio
5. Clique no botão de download

---

### Download de Playlist

1. Marque a opção **Playlist** no painel lateral  
2. Cole o link da playlist no campo principal  
3. Selecione o formato desejado (MP4, M4A ou ambos)
4. Clique no botão de download  
5. Aguarde a conclusão do processo

O programa fará o download de todos os vídeos automaticamente.

---

## 🔧 Recursos Extras

- **Abrir Pasta:**  
  Após finalizar os downloads, você pode abrir diretamente a pasta onde os arquivos foram salvos.

- **Limpar Cache:**  
  Caso ocorra algum erro, utilize o botão de limpar cache para reiniciar o estado do aplicativo.

- **Ver Informações:**  
  Um botão de informações está disponível com créditos do desenvolvedor.

---

## ⚠ Possíveis Problemas

Se você encontrar algum erro ao baixar vídeos:

- Verifique se o link é válido  
- Certifique-se de estar conectado à internet  
- Use o botão de limpar cache e tente novamente  
- Confirme que selecionou pelo menos um formato (MP4 ou M4A)

---

## 📁 Estrutura do Projeto

```
SimplyTube/
│
├── Assets/                # Imagens e ícones da interface
├── main.py                # Código principal da aplicação
└── README.md              # Documentação
```


---

## 📄 Licença

Este projeto é de uso livre para fins educacionais, pessoais e para baixar conteúdo que você tem permissão para baixar. 
Respeite os direitos autorais e os termos de serviço do YouTube.


⭐ Se você gostou deste projeto, considere dar uma estrela no repositório!
