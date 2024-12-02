
-- Insercao dos dados
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (1, 'J.K. Rowling', '1965-07-31');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (2, 'George R.R. Martin', '1948-09-20');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (3, 'J.R.R. Tolkien', '1892-01-03');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (1, 'Fantasia');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (2, 'Ficção Científica');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (3, 'Aventura');
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (1, 'Harry Potter e a Pedra Filosofal', 1, 1997);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (2, 'A Guerra dos Tronos', 2, 1996);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (3, 'O Senhor dos Anéis', 3, 1954);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (1, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (1, 3);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (2, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (2, 2);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (3, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (3, 3);
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (1, 'Alice', 'alice@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (2, 'Bob', 'bob@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (3, 'Charlie', 'charlie@example.com');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (1, 1, 1, '2024-07-01', '2024-07-10');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (2, 2, 2, '2024-07-05', '2024-07-15');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (3, 3, 3, '2024-07-10', NULL);

-- NOVAS INSERÇÔES

INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (4, 'Isaac Asimov', '1920-01-02');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (5, 'Arthur C. Clarke', '1917-12-16');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (6, 'Agatha Christie', '1890-09-15');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (7, 'Neil Gaiman', '1960-11-10');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (8, 'Dan Brown', '1964-06-22');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (9, 'Stephen King', '1947-09-21');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (10, 'Margaret Atwood', '1939-11-18');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (11, 'Frank Herbert', '1920-10-08');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (12, 'H.G. Wells', '1866-09-21');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (13, 'Suzanne Collins', '1962-08-10');

INSERT INTO Categoria (ID_Categoria, Nome) VALUES (4, 'Mistério');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (5, 'Terror');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (6, 'Biografia');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (7, 'Romance Histórico');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (8, 'Suspense');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (9, 'Distopia');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (10, 'Literatura Infantil');

INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (4, 'Fundação', 4, 1951);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (5, '2001: Uma Odisseia no Espaço', 5, 1968);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (6, 'Assassinato no Expresso do Oriente', 6, 1934);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (7, 'Deuses Americanos', 7, 2001);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (8, 'O Código Da Vinci', 8, 2003);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (9, 'It: A Coisa', 9, 1986);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (10, 'O Conto da Aia', 10, 1985);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (11, 'Duna', 11, 1965);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (12, 'A Máquina do Tempo', 12, 1895);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (13, 'Jogos Vorazes', 13, 2008);

INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (4, 'Diana', 'diana@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (5, 'Eve', 'eve@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (6, 'Frank', 'frank@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (7, 'Grace', 'grace@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (8, 'Hank', 'hank@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (9, 'Ivy', 'ivy@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (10, 'Jack', 'jack@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (11, 'Karen', 'karen@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (12, 'Leo', 'leo@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (13, 'Mia', 'mia@example.com');

INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (4, 4, 4, '2024-07-15', NULL);
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (5, 5, 5, '2024-07-18', '2024-07-25');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (6, 6, 6, '2024-07-20', NULL);
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (7, 7, 7, '2024-07-21', '2024-07-28');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (8, 8, 8, '2024-07-22', NULL);
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (9, 9, 9, '2024-07-23', NULL);
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (10, 10, 10, '2024-07-24', '2024-07-31');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (11, 11, 11, '2024-07-25', NULL);
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (12, 12, 12, '2024-07-26', '2024-08-02');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (13, 13, 13, '2024-07-27', NULL);
