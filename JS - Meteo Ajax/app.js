function main() {
    //récupérer l'adresse IP du PC qui ouvre la page
    fetch('https://api.ipify.org?format=json')
        .then(resultat => resultat.json())
        .then(json => {
            const ip = json.ip;

            fetch('http://ip-api.com/json/' + ip)
                .then(resultat => resultat.json())
                .then(json => {
                    const ville = json.city;

                    fetch('http://api.openweathermap.org/data/2.5/weather?q=' + ville + '?id=524901&appid=c34d33634a666867732e2573934b0b16&lang=fr&units=metric')
                        .then(resultat => console.log(resultat))
                })


        })

}

main()