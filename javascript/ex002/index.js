// console.log(process.argv) // Uncomment for debugging if needed

const username = process.argv[2];

if (!username) {
    console.log("Porfavor, insira um nome de usuário.")
    process.exit(1)
}

console.log(`Procurando atividade de ${username}...`)

async function procuraGithub() {
    const url = `https://api.github.com/users/${username}/events`;

    const response = await fetch(url);

    // console.log(response.status)
    
    const events = await response.json();

    // console.log(events);
    console.log(events[0]);


}

procuraGithub();
