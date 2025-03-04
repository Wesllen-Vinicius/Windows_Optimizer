# Windows Optimizer

## 📌 Descrição

Este script otimiza o desempenho de computadores Windows voltados para jogos e desenvolvimento de software. Ele realiza as seguintes ações:

✅ **Limpeza de arquivos temporários** para liberar espaço em disco.
✅ **Liberação de memória RAM** utilizando chamadas nativas do Windows.
✅ **Desativação de serviços desnecessários** para reduzir consumo de CPU e disco.
✅ **Opção de restaurar serviços** caso seja necessário reverter mudanças.

---

## ⚙️ Requisitos

Para executar este script, você precisa:

- Windows 10 ou superior.
- Python 3.8 ou superior instalado.

---

## 🛠️ Configuração da Virtual Environment (venv)

É altamente recomendado executar o script dentro de um ambiente virtual Python. Para configurar:

1. **Criar um ambiente virtual**:
   ```bash
   python -m venv venv
   ```
2. **Ativar o ambiente virtual**:
   - No **Windows (CMD ou PowerShell)**:
     ```bash
     venv\Scripts\activate
     ```
   - No **Git Bash ou outro terminal compatível**:
     ```bash
     source venv/Scripts/activate
     ```
3. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

Se não houver um arquivo `requirements.txt`, as principais bibliotecas podem ser instaladas com:

```bash
pip install psutil
```

---

## 🚀 Como Executar

### **Execução Normal**

1. **Abra o terminal (CMD, PowerShell ou Terminal do VS Code)**.
2. **Ative o ambiente virtual (caso esteja usando venv)**.
3. **Execute o script**:
   ```bash
   python windows_optimizer.py
   ```

### **Opção para Restaurar Serviços**

Se precisar restaurar os serviços que foram desativados:

```bash
python windows_optimizer.py --restore
```

---

## ❗ Observações Importantes

- **Execução sem privilégios administrativos**: O script pode ser executado normalmente sem permissões elevadas.
- **Liberação de RAM**: Utiliza chamadas nativas do Windows via `NtSetSystemInformation` e `wmic`.
- **Nenhuma modificação permanente no sistema**: É possível restaurar qualquer mudança feita pelo script.

---

## 📩 Contato

Caso tenha dúvidas ou precise de suporte, sinta-se à vontade para contribuir ou abrir uma issue no repositório.

## 🔹 **Autor:** Wesllen Lima

# Windows Optimizer (English Version)

## 📌 Description

This script optimizes the performance of Windows computers for gaming and software development. It performs the following actions:

✅ **Cleans temporary files** to free up disk space.
✅ **Frees up RAM** using native Windows calls.
✅ **Disables unnecessary services** to reduce CPU and disk usage.
✅ **Provides an option to restore services** if needed.

---

## ⚙️ Requirements

To run this script, you need:

- Windows 10 or later.
- Python 3.8 or later installed.

---

## 🛠️ Virtual Environment (venv) Setup

It is highly recommended to run the script within a Python virtual environment. To set it up:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment**:
   - On **Windows (CMD or PowerShell)**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Git Bash or another compatible terminal**:
     ```bash
     source venv/Scripts/activate
     ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

If there is no `requirements.txt` file, the main dependencies can be installed with:

```bash
pip install psutil
```

---

## 🚀 How to Run

### **Normal Execution**

1. **Open the terminal (CMD, PowerShell, or VS Code Terminal)**.
2. **Activate the virtual environment (if using venv)**.
3. **Run the script**:
   ```bash
   python windows_optimizer.py
   ```

### **Restore Services Option**

If you need to restore the disabled services:

```bash
python windows_optimizer.py --restore
```

---

## ❗ Important Notes

- **No admin privileges required**: The script runs normally without elevated permissions.
- **RAM optimization**: Uses native Windows calls (`NtSetSystemInformation` and `wmic`).
- **No permanent system modifications**: Any changes made by the script can be restored.

---

## 📩 Contact

If you have any questions or need support, feel free to contribute or open an issue in the repository.

🔹 **Author:** Wesllen Lima
