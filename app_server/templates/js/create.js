const editor = ace.edit('editor', {
    mode: 'ace/mode/json',
    selectionStyle: 'text',
    showPrintMargin: false,
    theme: 'ace/theme/chrome'
  })
  
  const formatText = (spacing = 0) => {
    try {
      const current = JSON.parse(editor.getValue())
      editor.setValue(JSON.stringify(current, null, spacing))
      editor.focus()
      editor.selectAll()
      document.execCommand('copy')
    } catch (err) {
      alert('ERROR: Unable to parse text as JSON')
    }
  }
  
  editor.on('paste', (event) => {
    try {
      event.text = JSON.stringify(JSON.parse(event.text), null, 4)
    } catch (err) {
      // meh
    }
  })
  
  document.getElementById('minify').addEventListener('click', () => formatText())
  document.getElementById('beautify').addEventListener('click', () => formatText(4))