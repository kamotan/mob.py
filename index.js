const Discord = require('discord.js');
const client = new Discord.Client({ws: { intents: ["GUILDS", "GUILD_MESSAGES", "GUILD_MEMBERS"] }});

client.login("OTg3OTgzNTA0NTg5NTkwNTY4.G7-Kca.sAXd-Rq11h_nIvP0rP2mk3HL6jN2a_DcaNX1w8");

client.on('ready', () => {
    console.log(`${client.user.tag}`);
});

client.on('messageCreate', message => {
    if (message.author.bot) return;
    if (message.content.includes('あから始まるモブウマ娘')) {
        if(message.channel.name === 'モブウマ娘博士BOTの部屋'){
        message.reply('アーケードチャンプ');
        }
    }
});