-- Listar todos os livros com seus autores:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor
inner join Livro ON autor.ID_autor = livro.id_autor;

-- Listar todos os empréstimos e os usuários correspondentes:
SELECT Emprestimo.ID_Emprestimo, Usuario.Nome 
FROM Emprestimo
inner join usuario on emprestimo.id_usuario = usuario.id_usuario;

-- Listar todos os livros e suas categorias:
SELECT Livro.Titulo, Categoria.Nome
FROM Livro
inner join livro_categoria on Livro.ID_Livro = Livro_Categoria.ID_Livro
inner join categoria on Livro_Categoria.ID_Categoria = Categoria.ID_Categoria;

-- Listar todos os livros emprestados:

SELECT Livro.Titulo, Usuario.Nome 
from livro
inner join emprestimo on Livro.ID_Livro = Emprestimo.ID_Livro 
inner join usuario on Emprestimo.ID_Usuario = Usuario.ID_Usuario;


-- LIstar os livros emprestados sem data de devolução
SELECT l.titulo as livro, u.nome as Usuario, e.data_emprestimo
from Livro as l
inner join emprestimo as e on l.id_livro = e.id_livro
inner join usuario as u on u.id_usuario = e.id_usuario
where e.data_devolucao is null;

-- Listar livros emprestados de fantasia

select l.titulo as livro, u.nome as usuario, c.nome as categoria
from livro as l
inner join emprestimo as e on l.id_livro = e.id_livro
inner join usuario as u on u.id_usuario = e.id_usuario
inner join livro_categoria as l_c on l_c.id_livro = l.id_livro
inner join categoria as c on l_c.id_categoria = c.id_categoria
where c.nome = "Fantasia";