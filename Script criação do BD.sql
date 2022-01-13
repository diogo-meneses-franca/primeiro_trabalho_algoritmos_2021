USE cadastro;

create table if not exists pessoas(
`id` int not null auto_increment,
`nome` varchar(100) not null,
`cpf` varchar(14),
`endereco` varchar(200),
`numero_casa` varchar(10),
`cidade` varchar(100),
`estado` varchar(100),
`pais` varchar(100) default 'Brasil',
primary key(id)) default char set = utf8mb4;

select * from pessoas;