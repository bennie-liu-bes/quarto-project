# 產生 docx 範本檔案

```
quarto pandoc -o custom-reference-doc.docx --print-default-data-file reference.docx
```

# docx 檔中 TOC 顯示在第二頁

範本中建立目錄，在目錄標題樣式中，設定 格式>段落>分行與分頁設定>段落前分頁 勾選

# 多格式輸出

1. 設定 formats: pdf, docx, html

1. vscode 安裝 quarto 插件後執行 Quarto: Render

# 使用 plugin

每個專案都需個別安裝 plugin，安裝內容在\_extensions 資料夾中
