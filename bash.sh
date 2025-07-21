#!/bin/bash

# Список вебсайтів
websites=("https://google.com" "https://facebook.com" "https://twitter.com")

# Назва файлу логів
log_file="website_status.log"

# Очищаємо старий лог-файл
> "$log_file"

# Перевіряємо кожен сайт
for site in "${websites[@]}"; do
    # Виконуємо запит curl
    http_status=$(curl -s -o /dev/null -w "%{http_code}" -L "$site")
    
    # Перевіряємо статус-код
    if [ "$http_status" -eq 200 ]; then
        echo "<$site> is UP" >> "$log_file"
    else
        echo "<$site> is DOWN" >> "$log_file"
    fi
done

# Виводимо повідомлення про завершення
echo "Результати записано у файл логів: $log_file"
