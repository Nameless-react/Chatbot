./bin/ollama serve &

pid=$!

sleep 5
if ! ollama list | grep -q "llama3.1"; then
    echo "Descargando el modelo llama3.1..."
    ollama pull llama3.1
else
    echo "El modelo llama3.1 ya está presente."
fi
wait $pid