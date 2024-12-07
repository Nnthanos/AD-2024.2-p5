-- Listar todos os livros com seus autores:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor
right join Livro ON autor.ID_autor = livro.id_autor;

-- Listar todos os empréstimos e os usuários correspondentes:
SELECT Emprestimo.ID_Emprestimo, Usuario.Nome 
FROM Emprestimo
left join usuario on emprestimo.id_usuario = usuario.id_usuario;

-- Listar todos os livros e suas categorias:
SELECT Livro.Titulo, Categoria.Nome
FROM Livro
LEFT join livro_categoria on Livro.ID_Livro = Livro_Categoria.ID_Livro
LEFT join categoria on Livro_Categoria.ID_Categoria = Categoria.ID_Categoria; -- Garante que todos os livros sejam listados mesmo sem categoria

-- Listar todos os livros emprestados:
SELECT Livro.Titulo, Usuario.Nome 
from livro
inner join emprestimo on Livro.ID_Livro = Emprestimo.ID_Livro 
inner join usuario on Emprestimo.ID_Usuario = Usuario.ID_Usuario
where emprestimo.id_emprestimo is not null;


-- LIstar os livros emprestados sem data de devolução
SELECT l.titulo as livro, u.nome as Usuario, e.data_emprestimo
from Livro as l
inner join emprestimo as e on l.id_livro = e.id_livro
inner join usuario as u on u.id_usuario = e.id_usuario
where e.data_devolucao is null;

-- Listar livros emprestados de fantasia

SELECT l.titulo AS livro, u.nome AS usuario, c.nome AS categoria
FROM Livro AS l
INNER JOIN Livro_Categoria AS l_c ON l_c.ID_Livro = l.ID_Livro
LEFT JOIN Categoria AS c ON l_c.ID_Categoria = c.ID_Categoria
LEFT JOIN Emprestimo AS e ON l.ID_Livro = e.ID_Livro
LEFT JOIN Usuario AS u ON e.ID_Usuario = u.ID_Usuario
WHERE c.nome = "Fantasia";

-- Listar os autores que tem livros emprestados

select a.nome as Autor, l.titulo as nome, e.data_emprestimo
from autor as a
inner join livro as l on a.id_autor = l.id_autor
LEFT join emprestimo as e on l.id_livro = e.id_livro
where e.data_devolucao is null;