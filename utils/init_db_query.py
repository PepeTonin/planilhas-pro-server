create_table_query = """
CREATE TABLE IF NOT EXISTS professores (
    professorId INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    dataCadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    ativo TINYINT(1) DEFAULT 1
);

CREATE TABLE IF NOT EXISTS alunos (
    alunoId INT PRIMARY KEY AUTO_INCREMENT,
    firebaseId VARCHAR(30) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    dataNascimento DATE,
    dataCadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    situacaoPagamento ENUM('ativo', 'inativo', 'atrasado') DEFAULT 'ativo',
    situacaoTreino ENUM('regular', 'treino pendente', 'suporte necessario') DEFAULT 'regular',
    ativo TINYINT(1) DEFAULT 1,
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS grupos (
    grupoId INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS sub_grupos (
    subGrupoId INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    grupoId INT,
    FOREIGN KEY (grupoId)
        REFERENCES grupos (grupoId)
);

CREATE TABLE IF NOT EXISTS alunos_grupos (
    alunoId INT,
    grupoId INT,
    PRIMARY KEY (alunoId , grupoId),
    FOREIGN KEY (alunoId)
        REFERENCES alunos (alunoId),
    FOREIGN KEY (grupoId)
        REFERENCES grupos (grupoId)
);

CREATE TABLE IF NOT EXISTS alunos_sub_grupos (
    alunoId INT,
    subGrupoId INT,
    PRIMARY KEY (alunoId , subGrupoId),
    FOREIGN KEY (alunoId)
        REFERENCES alunos (alunoId),
    FOREIGN KEY (subGrupoId)
        REFERENCES sub_grupos (subGrupoId)
);

CREATE TABLE IF NOT EXISTS movimentos (
    movimentoId INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS descricoes_movimentos (
    descricaoMovimentoId INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(255) NOT NULL,
    movimentoId INT NOT NULL,
    FOREIGN KEY (movimentoId)
        REFERENCES movimentos (movimentoId)
);

CREATE TABLE IF NOT EXISTS treinos (
    treinoId INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS treino_categorias (
    categoriaId INT PRIMARY KEY AUTO_INCREMENT,
    label VARCHAR(100) NOT NULL,
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS treino_categoria_relacionamentos (
    treinoId INT NOT NULL,
    categoriaId INT NOT NULL,
    PRIMARY KEY (treinoId , categoriaId),
    FOREIGN KEY (treinoId)
        REFERENCES treinos (treinoId),
    FOREIGN KEY (categoriaId)
        REFERENCES treino_categorias (categoriaId)
);

CREATE TABLE IF NOT EXISTS treino_movimento_relacionamentos (
    treinoId INT NOT NULL,
    movimentoId INT NOT NULL,
    PRIMARY KEY (treinoId , movimentoId),
    FOREIGN KEY (treinoId)
        REFERENCES treinos (treinoId),
    FOREIGN KEY (movimentoId)
        REFERENCES movimentos (movimentoId)
);

CREATE TABLE IF NOT EXISTS planilhas (
    planilhaId INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS planilha_categorias (
    categoriaId INT PRIMARY KEY AUTO_INCREMENT,
    label VARCHAR(100) NOT NULL,
    professorId INT,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS planilha_categoria_relacionamentos (
    planilhaId INT NOT NULL,
    categoriaId INT NOT NULL,
    PRIMARY KEY (planilhaId , categoriaId),
    FOREIGN KEY (planilhaId)
        REFERENCES planilhas (planilhaId),
    FOREIGN KEY (categoriaId)
        REFERENCES planilha_categorias (categoriaId)
);

CREATE TABLE IF NOT EXISTS modelos_planilha (
    modeloPlanilhaId INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    planilhaId INT NOT NULL,
    FOREIGN KEY (planilhaId)
        REFERENCES planilhas (planilhaId),
    professorId INT NOT NULL,
    FOREIGN KEY (professorId)
        REFERENCES professores (professorId)
);

CREATE TABLE IF NOT EXISTS alunos_planilhas (
	alunoPlanilhaRelacionamentoId INT PRIMARY KEY AUTO_INCREMENT,
    alunoId INT NOT NULL,
    planilhaId INT NOT NULL,
    dataInicio DATE NOT NULL,
    dataFim DATE NOT NULL,
    FOREIGN KEY (alunoId)
        REFERENCES alunos (alunoId),
    FOREIGN KEY (planilhaId)
        REFERENCES planilhas (planilhaId)
);

CREATE TABLE IF NOT EXISTS sessoes (
    sessaoId INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    planilhaId INT NOT NULL,
    FOREIGN KEY (planilhaId)
        REFERENCES planilhas (planilhaId)
);

CREATE TABLE IF NOT EXISTS blocos_treino (
    blocoTreinoId INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    sessaoId INT NOT NULL,
    treinoId INT NOT NULL,
    FOREIGN KEY (sessaoId)
        REFERENCES sessoes (sessaoId),
	FOREIGN KEY (treinoId)
        REFERENCES treinos (treinoId)
);

-- Inserir o Professor
INSERT INTO professores (nome, email, senha)
VALUES ('Pedro Tonin', 'professor@email.com', 'senha123');

-- Inserir Alunos
INSERT INTO alunos (firebaseId, nome, email, senha, dataNascimento, ativo, professorId)
VALUES 
    ('UBrZl59cTuVlR3dhAzFaj9TL52s1', 'Maria Oliveira', 'mariaoliveira@email.com', 'senha123', '2000-05-10', 1, 1),  -- id 1
    ('L91GvlBOy1QiLwCOLXi1qqriHeq2', 'Carlos Souza', 'carlossouza@email.com', 'senha123', '1998-08-15', 1, 1),      -- id 2
    ('uAVT9BGKaHasaLT0OcCFxwzyGHM2', 'Ana Costa', 'anacosta@email.com', 'senha123', '2001-03-20', 1, 1),            -- id 3
    ('j15W3klojySez4A41Vg9VM3gvzy1', 'Lucas Pereira', 'lucaspereira@email.com', 'senha123', '1997-12-05', 1, 1),    -- id 4
    ('JXoTjzg0rJf7AEBAkZVb7zgIJP53', 'Fernanda Lima', 'fernandalima@email.com', 'senha123', '1999-07-30', 1, 1),    -- id 5
    ('hDHkY8evcNal52r3MxnBJbusDpq1', 'Pedro Alves', 'pedroalves@email.com', 'senha123', '2002-01-14', 1, 1),        -- id 6
    ('pom9ATZ9opYBqHbr1lIKyI3YNj12', 'Julia Martins', 'juliamartins@email.com', 'senha123', '2003-04-22', 1, 1),    -- id 7
    ('ky0bpQCHd3QcTm51li7B4jFHjNs1', 'Rafael Gomes', 'rafaelgomes@email.com', 'senha123', '1996-11-30', 1, 1),      -- id 8
    ('3o8Y8318JsYKeWFvX3ZgyDiRyW92', 'Sofia Lima', 'sofialima@email.com', 'senha123', '1995-02-14', 1, 1),          -- id 9
    ('gQ72nbTtFuQdNMXF2StnyzvXxH02', 'Gustavo Silva', 'gustavosilva@email.com', 'senha123', '1994-09-01', 1, 1),    -- id 10
    ('LNfzmFNvCmYtP9vF8ouZFoLDmwK2', 'Isabela Costa', 'isabelacosta@email.com', 'senha123', '2004-06-18', 1, 1);    -- id 11

-- Inserir Grupos
INSERT INTO grupos (nome, professorId)
VALUES 
    ('Corrida', 1),     -- id 1
    ('Triathlon', 1),   -- id 2
    ('Academia', 1);    -- id 3

-- Inserir Subgrupos
INSERT INTO sub_grupos (nome, grupoId)
VALUES 
    ('Iniciante', 1),           -- id 1
    ('Intermediário', 1),       -- id 2
    ('Avançado', 1),            -- id 3
    ('Intermediário short', 2), -- id 4
    ('Intermediário 70.3', 2),  -- id 5
    ('Hipertrofia', 3),         -- id 6
    ('Full body', 3);           -- id 7

-- Associar Alunos a Grupos
INSERT INTO alunos_grupos (alunoId, grupoId)
VALUES 
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 2),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 3),
    (10, 3),
    (11, 3);

-- Associar Alunos a Subgrupos
INSERT INTO alunos_sub_grupos (alunoId, subGrupoId)
VALUES 
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (6, 4),
    (7, 5),
    (8, 5),
    (9, 6),
    (10, 7),
    (11, 7);

-- Inserir Movimentos / exercícios -> refatorar algum dia
INSERT INTO movimentos (titulo, professorId)
VALUES 
    ('Aquecimento de corrida iniciante', 1),
    ('Aquecimento de corrida intermediário', 1),
    ('Aquecimento de corrida avançado', 1),
    ('Treino de tiro em pista iniciante - 10x200m', 1),
    ('Treino de tiro em pista intermediário - 10x400m', 1),
    ('Treino de tiro em pista avançado - 10x400m', 1),
	('Fartlek iniciante', 1),
    ('Fartlek intermediário', 1),
    ('Fartlek avançado', 1),
    ('Rodagem de corrida confortável iniciante', 1),
    ('Rodagem de corrida confortável intermediário', 1),
    ('Rodagem de corrida confortável avançado', 1),
    ('Longão de corrida iniciante 6k', 1),
    ('Longão de corrida intermediário 12k', 1),
    ('Longão de corrida avançado 21k', 1),
    ('Desaquecimento de corrida generico', 1),
    ('Aquecimento de natação iniciante com acessorio', 1),
    ('Aquecimento de natação intermediário com acessorio', 1),
    ('Aquecimento de natação iniciante', 1),
    ('Aquecimento de natação intermediário', 1),
    ('Aquecimento de natação avançado', 1),
    ('Treino de técnica de natação iniciante', 1),
    ('Treino de técnica de natação intermediário', 1),
    ('Treino de técnica de natação avançado', 1),
    ('Treino de endurance de natação iniciante - 10x50m', 1),
    ('Treino de endurance de natação intermediário - 5x200m', 1),
    ('Treino de endurance de natação avançado - 3x800m', 1),
    ('Rodagem de natação confortável iniciante', 1),
    ('Rodagem de natação confortável intermediário', 1),
    ('Rodagem de natação confortável avançado', 1),
    ('Desaquecimento de natação genérico', 1),
    ('Aquecimento de ciclismo iniciante', 1),
    ('Aquecimento de ciclismo intermediário', 1),
    ('Aquecimento de ciclismo avançado', 1),
    ('Treino de cadência de ciclismo iniciante', 1),
    ('Treino de cadência de ciclismo intermediário', 1),
    ('Treino de cadência de ciclismo avançado', 1),
    ('Treino de subida de ciclismo iniciante', 1),
    ('Treino de subida de ciclismo intermediário', 1),
    ('Treino de subida de ciclismo avançado', 1),
    ('Longão de ciclismo iniciante 20km', 1),
    ('Longão de ciclismo intermediário 40km', 1),
    ('Longão de ciclismo avançado 90km', 1),
    ('Desaquecimento de ciclismo genérico', 1),
    ('Aquecimento de academia iniciante', 1),
    ('Aquecimento de academia intermediário', 1),
    ('Aquecimento de academia avançado', 1),
    ('Levantamento terra iniciante', 1),
    ('Levantamento terra intermediário', 1),
    ('Levantamento terra avançado', 1),
    ('Agachamento livre iniciante', 1),
    ('Agachamento livre intermediário', 1),
    ('Agachamento livre avançado', 1),
    ('Extensão de quadril iniciante', 1),
    ('Extensão de quadril intermediário', 1),
    ('Extensão de quadril avançado', 1),
    ('Leg press iniciante', 1),
    ('Leg press intermediário', 1),
    ('Leg press avançado', 1),
    ('Supino reto iniciante', 1),
    ('Supino reto intermediário', 1),
    ('Supino reto avançado', 1),
    ('Supino inclinado iniciante', 1),
    ('Supino inclinado intermediário', 1),
    ('Supino inclinado avançado', 1),
    ('Rosca direta iniciante', 1),
    ('Rosca direta intermediário', 1),
    ('Rosca direta avançado', 1),
    ('Tríceps testa iniciante', 1),
    ('Tríceps testa intermediário', 1),
    ('Tríceps testa avançado', 1),
    ('Remada curvada iniciante', 1),
    ('Remada curvada intermediário', 1),
    ('Remada curvada avançado', 1),
    ('Desenvolvimento de ombros iniciante', 1),
    ('Desenvolvimento de ombros intermediário', 1),
    ('Desenvolvimento de ombros avançado', 1),
    ('Elevação lateral iniciante', 1),
    ('Elevação lateral intermediário', 1),
    ('Elevação lateral avançado', 1),
    ('Puxada alta iniciante', 1),
    ('Puxada alta intermediário', 1),
    ('Puxada alta avançado', 1),
    ('Abdominal supra iniciante', 1),
    ('Abdominal supra intermediário', 1),
    ('Abdominal supra avançado', 1),
    ('Prancha abdominal iniciante', 1),
    ('Prancha abdominal intermediário', 1),
    ('Prancha abdominal avançado', 1),
    ('Flexão de braço iniciante', 1),
    ('Flexão de braço intermediário', 1),
    ('Flexão de braço avançado', 1),
    ('Afundo iniciante', 1),
    ('Afundo intermediário', 1),
    ('Afundo avançado', 1),
    ('Stiff iniciante', 1),
    ('Stiff intermediário', 1),
    ('Stiff avançado', 1),
    ('Pullover iniciante', 1),
    ('Pullover intermediário', 1),
    ('Pullover avançado', 1),
    ('Crossover iniciante', 1),
    ('Crossover intermediário', 1),
    ('Crossover avançado', 1),
    ('Barra fixa iniciante', 1),
    ('Barra fixa intermediário', 1),
    ('Barra fixa avançado', 1),
    ('Abdominal remador iniciante', 1),
    ('Abdominal remador intermediário', 1),
    ('Abdominal remador avançado', 1),
    ('Desaquecimento de academia genérico', 1);

-- Inserir Descrições de Movimentos
INSERT INTO descricoes_movimentos (descricao, movimentoId)
VALUES 
    ('2km pace entre 6:30-7:00', 1),
    ('2km pace entre 6:20-6:30', 2),
    ('2km pace entre 6:00-6:10', 3),
    ('Fazer cada tiro em no máximo 1min', 4),
    ('Descanso de 2 mins entre cada tiro', 4),
    ('Fazer cada tiro em no máximo 1:50 ', 5),
    ('Descanso de 1 min entre cada tiro', 5),
    ('Fazer cada tiro em no máximo 1:20 ', 6),
    ('Descanso de 1 min entre cada tiro', 6),
    ('começa com: 400m trote', 7),
    ('logo em seguida: 200m correndo forte',7),
    ('fecha com: 200m caminhando', 7),
    ('repita 5 vezes', 7),
    ('começa com: 400m a 5:40-6:00', 8),
    ('logo em seguida: 200m forte 4:30-5:00',8),
    ('fecha com: 200m trote 6:20-6:30', 8),
    ('repita 10 vezes', 8),
    ('começa com: 400m a 5:00-5:10', 9),
    ('logo em seguida: 200m forte 3:30-3:40',9),
    ('fecha com: 200m trote 5:40-5:50', 9),
    ('repita 10 vezes', 9),
    ('4km bem leve sem controlar pace', 10),
    ('pode intercalar com caminhada', 10),
    ('6km a 6:00-6:30', 11),
    ('8km a 6:00-6:30', 12),
    ('6km a pace 6:30-7:00', 13),
    ('12km a pace 5:50-6:00', 14),
    ('21km a pace 5:10-5:20', 15),
    ('1km bem leve só pra soltar', 16),
    ('Aqueça com 5 minutos de natação leve utilizando flutuador', 17),
    ('Aqueça com 8 minutos de natação leve sem acessório', 18),
    ('Aqueça com 10 minutos de natação suave', 19),
    ('Treino técnico de natação com 8x50m focando na posição do corpo', 20),
    ('Treino técnico de natação com 6x100m, alternando braçadas e respiração', 21),
    ('Treino técnico de natação com 4x200m de técnica de pernada', 22),
    ('Endurance de natação com 10x50m, descansando 30s entre cada', 23),
    ('Endurance de natação com 5x200m, descansando 1min entre cada', 24),
    ('Endurance de natação com 3x800m, descansando 2min entre cada', 25),
    ('Rodagem de natação confortável com 15min alternando nado livre e costas', 26),
    ('Rodagem de natação confortável com 20min em ritmo suave', 27),
    ('Rodagem de natação confortável com 30min alternando nado peito e livre', 28),
    ('Desacelere com 5min de nado livre seguido de alongamento', 29),
    ('Aqueça com 5 minutos de ciclismo leve', 30),
    ('Aqueça com 10 minutos de ciclismo leve', 31),
    ('Aqueça com 15 minutos de ciclismo leve', 32),
    ('Treino de cadência com 5x1min a cadência de 90-100 rpm', 33),
    ('Treino de cadência com 5x2min a cadência de 100-110 rpm', 34),
    ('Treino de cadência com 5x3min a cadência de 110-120 rpm', 35),
    ('Treino de subida com 4x2min em subida de 5-7%', 36),
    ('Treino de subida com 5x3min em subida de 6-8%', 37),
    ('Treino de subida com 6x4min em subida de 8-10%', 38),
    ('Longão de ciclismo de 20km com ritmo suave', 39),
    ('Longão de ciclismo de 40km com ritmo moderado', 40),
    ('Longão de ciclismo de 90km com ritmo forte', 41),
    ('Desacelere com 10min de pedal leve', 42),
    ('Aqueça com 5 minutos de academia leve', 43),
    ('Aqueça com 8 minutos de academia leve', 44),
    ('Aqueça com 10 minutos de academia leve', 45),
    ('Levantamento terra com 3x12 repetições no ritmo moderado', 46),
    ('Levantamento terra com 4x10 repetições e peso progressivo', 47),
    ('Levantamento terra com 5x8 repetições e peso alto', 48),
    ('Agachamento livre com 3x15 repetições no ritmo leve', 49),
    ('Agachamento livre com 4x12 repetições e intensidade moderada', 50),
    ('Agachamento livre com 5x10 repetições e intensidade alta', 51),
    ('Extensão de quadril com 3x20 repetições de baixo impacto', 52),
    ('Extensão de quadril com 4x15 repetições e carga moderada', 53),
    ('Extensão de quadril com 5x10 repetições e carga alta', 54),
    ('Leg press com 3x12 repetições com carga leve', 55),
    ('Leg press com 4x10 repetições com carga moderada', 56),
    ('Leg press com 5x8 repetições com carga alta', 57),
    ('Supino reto com 3x15 repetições no ritmo leve', 58),
    ('Supino reto com 4x12 repetições e carga moderada', 59),
    ('Supino reto com 5x10 repetições e carga alta', 60),
    ('Supino inclinado com 3x15 repetições no ritmo leve', 61),
    ('Supino inclinado com 4x12 repetições e carga moderada', 62),
    ('Supino inclinado com 5x10 repetições e carga alta', 63),
    ('Rosca direta com 3x15 repetições e carga leve', 64),
    ('Rosca direta com 4x12 repetições e carga moderada', 65),
    ('Rosca direta com 5x10 repetições e carga alta', 66),
    ('Tríceps testa com 3x12 repetições e carga leve', 67),
    ('Tríceps testa com 4x10 repetições e carga moderada', 68),
    ('Tríceps testa com 5x8 repetições e carga alta', 69),
    ('Remada curvada com 3x12 repetições e carga moderada', 70),
    ('Remada curvada com 4x10 repetições e carga alta', 71),
    ('Remada curvada com 5x8 repetições e carga alta', 72),
    ('Desenvolvimento de ombros com 3x15 repetições e carga leve', 73),
    ('Desenvolvimento de ombros com 4x12 repetições e carga moderada', 74),
    ('Desenvolvimento de ombros com 5x10 repetições e carga alta', 75),
    ('Elevação lateral com 3x15 repetições e carga leve', 76),
    ('Elevação lateral com 4x12 repetições e carga moderada', 77),
    ('Elevação lateral com 5x10 repetições e carga alta', 78),
    ('Puxada alta com 3x15 repetições e carga leve', 79),
    ('Puxada alta com 4x12 repetições e carga moderada', 80),
    ('Puxada alta com 5x10 repetições e carga alta', 81),
    ('Abdominal supra com 3x20 repetições e ritmo moderado', 82),
    ('Abdominal supra com 4x15 repetições e intensidade alta', 83),
    ('Abdominal supra com 5x12 repetições e carga alta', 84),
    ('Prancha abdominal com 3x30s e intensidade moderada', 85),
    ('Prancha abdominal com 4x45s e intensidade alta', 86),
    ('Prancha abdominal com 5x60s e intensidade máxima', 87),
    ('Flexão de braço com 3x20 repetições e ritmo leve', 88),
    ('Flexão de braço com 4x15 repetições e carga moderada', 89),
    ('Flexão de braço com 5x10 repetições e carga alta', 90),
    ('Afundo com 3x12 repetições e carga leve', 91),
    ('Afundo com 4x10 repetições e carga moderada', 92),
    ('Afundo com 5x8 repetições e carga alta', 93),
    ('Stiff com 3x15 repetições e carga leve', 94),
    ('Stiff com 4x12 repetições e carga moderada', 95),
    ('Stiff com 5x10 repetições e carga alta', 96),
    ('Pullover com 3x15 repetições e carga leve', 97),
    ('Pullover com 4x12 repetições e carga moderada', 98),
    ('Pullover com 5x10 repetições e carga alta', 99);

-- Inserir Treinos
INSERT INTO treinos (titulo, descricao, professorId)
VALUES 
    ('Treino de tiro iniciante 10x200', 'Treino com foco no desenvolvimento da velocidade e melhora da capacidade cardio respiratória', 1),
    ('Treino de tiro intermediário 10x400', 'Treino com foco no desenvolvimento da velocidade e melhora da capacidade cardio respiratória', 1),
    ('Treino de tiro avançado 10x400', 'Treino com foco no desenvolvimento da velocidade e melhora da capacidade cardio respiratória', 1),
    ('Treino de corrida - longão iniciante', 'Treino em Z2 para melhorar cardio e resistência', 1),
    ('Treino de corrida - longão intermediário', 'Treino em Z2 para melhorar cardio e resistência', 1),
    ('Treino de corrida - longão avançado', 'Treino em Z2 para melhorar cardio e resistência', 1),
    ('Treino de corrida intervalado - iniciante', 'Treino para variar batimento cardiaco melhorando capacidade cardio respiratoria', 1),
    ('Treino de corrida intervalado - intermediário', 'Treino para variar batimento cardiaco melhorando capacidade cardio respiratoria', 1),
    ('Treino de corrida intervalado - avançado', 'Treino para variar batimento cardiaco melhorando capacidade cardio respiratoria', 1),
    ('Treino de hipertrofia - Peito e Tríceps', 'Treino focado em fortalecimento do peito e tríceps', 1),
    ('Treino de hipertrofia - Costas e Bíceps', 'Treino focado em fortalecimento das costas e bíceps', 1),
    ('Treino de hipertrofia - Pernas e Glúteos', 'Treino focado em fortalecimento das pernas e glúteos', 1),
    ('Treino de hipertrofia - Ombros e Abdômen', 'Treino focado em fortalecimento dos ombros e abdômen', 1),
    ('Treino de fortalecimento full body - Iniciante', 'Treino focado em fortalecimento do corpo inteiro, iniciante', 1),
    ('Treino de fortalecimento full body - Intermediário', 'Treino focado em fortalecimento do corpo inteiro, intermediário', 1),
    ('Treino de fortalecimento full body - Avançado', 'Treino focado em fortalecimento do corpo inteiro, avançado', 1),
    ('Treino de natação iniciante', 'Treino focado em fortalecimento do corpo inteiro, iniciante', 1),
    ('Treino de natação intermediário', 'Treino focado em fortalecimento do corpo inteiro, intermediário', 1),
    ('Treino de natação avançado', 'Treino focado em fortalecimento do corpo inteiro, avançado', 1),
    ('Treino de ciclismo iniciante', 'Treino focado em fortalecimento do corpo inteiro, iniciante', 1),
    ('Treino de ciclismo intermediário', 'Treino focado em fortalecimento do corpo inteiro, intermediário', 1),
    ('Treino de ciclismo avançado', 'Treino focado em fortalecimento do corpo inteiro, avançado', 1);

-- Inserir Movimentos em Treinos
INSERT INTO treino_movimento_relacionamentos (treinoId, movimentoId)
VALUES 
    (1,1),  
    (1,4),  
    (1,16), 
    (2,2),  
    (2,5),  
    (2,16), 
    (3,3),  
    (3,6),  
    (3,16), 
    (4,1),  
    (4,12), 
    (4,14), 
    (4,16), 
    (5,2),  
    (5,13), 
    (5,16), 
    (6,3),  
    (6,14), 
    (6,16), 
    (7,1),  
    (7,7),  
    (7,16), 
    (8,2),  
    (8,8),  
    (8,16), 
    (9,3),  
    (9,9),  
    (9,16), 
    (10,43),
    (10,44),
    (10,45),
	(11,70),
	(11,71),
	(11,72),
	(12,38),
	(12,39),
	(12,40),
	(13,52),
	(13,53),
	(13,54),
	(14,1),	 
	(14,17),
    (14,30),
	(15,19),
	(15,31),
	(16,21),
	(17,30),
	(18,31),
  	(19,32),
  	(20,34),
  	(21,35),
    (22,37);

-- Inserir Planilhas
INSERT INTO planilhas (titulo, descricao, professorId)
VALUES 
    ('Modelo', 'Planilha de treino com treino de segunda a sexta e descanço domingo', 1);

-- Inserir Sessões
INSERT INTO sessoes (titulo, planilhaId)
VALUES 
    ('Segunda-feira', 1),
    ('Terça-feira', 1),
    ('Quarta-feira', 1),
    ('Quinta-feira', 1),
    ('Sexta-feira', 1),
    ('Sábado', 1),
	('Domingo', 1);
  
-- Inserir Modelos de Planilha
INSERT INTO modelos_planilha (titulo, planilhaId, professorId)
VALUES 
    ('Modelo com sessões sendo os dias da semana', 1, 1);
"""

