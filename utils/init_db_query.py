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
    descricao VARCHAR(255) NOT NULL,
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
    descricao VARCHAR(255) NOT NULL,
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
        REFERENCES planilhas (planilhaId)
);

CREATE TABLE IF NOT EXISTS planilha_treino_relacionamentos (
    treinoId INT NOT NULL,
    planilhaId INT NOT NULL,
    PRIMARY KEY (treinoId , planilhaId),
    FOREIGN KEY (treinoId)
        REFERENCES treinos (treinoId),
    FOREIGN KEY (planilhaId)
        REFERENCES planilhas (planilhaId)
);
"""
