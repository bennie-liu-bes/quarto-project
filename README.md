# 產生docx範本檔案

```
quarto pandoc -o custom-reference-doc.docx --print-default-data-file reference.docx
```

# docx檔中TOC顯示在第二頁

範本中建立目錄，在目錄標題樣式中，設定 格式>段落>分行與分頁設定>段落前分頁 勾選

# 多格式輸出

1. 設定formats: pdf, docx, html

1. vscode安裝quarto插件後執行Quarto: Render