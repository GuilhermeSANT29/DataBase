/* =========================================================
   PROJETO PROFESSOR - BANCO COMPLETO SQL SERVER
   ========================================================= */

CREATE DATABASE automacao_industrial;
GO

USE automacao_industrial;
GO

/* =========================
   TABELA CLIENTES
========================= */
CREATE TABLE clientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf_cnpj VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(150),
    telefone VARCHAR(20),
    ativo BIT NOT NULL DEFAULT 1,
    inativado_em DATE NULL
);
GO

/* =========================
   TABELA EQUIPAMENTOS
========================= */
CREATE TABLE equipamentos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tag VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(200) NOT NULL,
    localizacao VARCHAR(100),
    tipo VARCHAR(20) NOT NULL,
    ativo BIT NOT NULL DEFAULT 1,
    instalado_em DATE NOT NULL,
    desativado_em DATE NULL,
    CONSTRAINT chk_tipo_equip
        CHECK (tipo IN ('sensor','atuador','controlador','medidor'))
);
GO

/* =========================
   LEITURAS SENSORES
========================= */
CREATE TABLE leituras_sensores (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    equipamento_id INT NOT NULL,
    valor DECIMAL(12,4) NOT NULL,
    unidade VARCHAR(20) NOT NULL,
    qualidade VARCHAR(10) NOT NULL DEFAULT 'bom',
    coletado_em DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    CONSTRAINT fk_leit_equip
        FOREIGN KEY (equipamento_id)
        REFERENCES equipamentos(id),
    CONSTRAINT chk_qualidade
        CHECK (qualidade IN ('bom','suspeito','ruim'))
);
GO

/* =========================
   NOTAS FISCAIS
========================= */
CREATE TABLE notas_fiscais (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id INT NOT NULL,
    numero_nf VARCHAR(20) NOT NULL UNIQUE,
    serie VARCHAR(5),
    valor_total DECIMAL(14,2) NOT NULL,
    emitida_em DATE NOT NULL,
    cancelada_em DATE NULL,
    CONSTRAINT fk_nf_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
);
GO

/* =========================
   BACKUPS
========================= */
CREATE TABLE backups (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    tamanho_mb DECIMAL(10,2),
    caminho_arquivo VARCHAR(500),
    iniciado_em DATETIME2 NOT NULL,
    finalizado_em DATETIME2 NULL,
    criado_em DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    CONSTRAINT chk_backup_tipo
        CHECK (tipo IN ('completo','incremental','diferencial')),
    CONSTRAINT chk_backup_status
        CHECK (status IN ('sucesso','falha','parcial'))
);
GO

/* =========================
   LOGS DE ACESSO
========================= */
CREATE TABLE logs_acesso (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    usuario VARCHAR(100) NOT NULL,
    acao VARCHAR(200) NOT NULL,
    tabela_afetada VARCHAR(100),
    registro_id INT NULL,
    ip_origem VARCHAR(45),
    resultado VARCHAR(10) NOT NULL DEFAULT 'sucesso',
    detalhes NVARCHAR(MAX),
    acessado_em DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    CONSTRAINT chk_resultado
        CHECK (resultado IN ('sucesso','negado','erro'))
);
GO

/* =========================
   REGISTRO DESCARTE LGPD
========================= */
CREATE TABLE registro_descarte (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tabela_origem VARCHAR(100) NOT NULL,
    criterio VARCHAR(300) NOT NULL,
    qtd_registros INT NOT NULL,
    autorizado_por VARCHAR(150) NOT NULL,
    area_autorizadora VARCHAR(30) NOT NULL,
    metodo_descarte VARCHAR(30) NOT NULL,
    descartado_em DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    observacao VARCHAR(MAX),
    CONSTRAINT chk_qtd CHECK (qtd_registros >= 0)
);
GO

/* =========================
   CLIENTES HISTÓRICO (LGPD)
========================= */
CREATE TABLE clientes_historico (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id_orig INT NOT NULL,
    nome_anonimizado VARCHAR(50) NOT NULL,
    inativado_em DATE NULL,
    arquivado_em DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);
GO

/* =========================
   ÍNDICES
========================= */
CREATE INDEX idx_logs_data ON logs_acesso(acessado_em);
CREATE INDEX idx_leituras_data ON leituras_sensores(coletado_em);
CREATE INDEX idx_nf_cliente ON notas_fiscais(cliente_id);
GO

/* =========================
   TRIGGER LOG CLIENTES
========================= */
CREATE TRIGGER trg_clientes_insert
ON clientes
AFTER INSERT
AS
BEGIN
    INSERT INTO logs_acesso (usuario, acao, tabela_afetada, registro_id, resultado, detalhes)
    SELECT SYSTEM_USER, 'INSERT', 'clientes', id, 'sucesso', nome
    FROM inserted;
END;
GO

CREATE TRIGGER trg_clientes_delete
ON clientes
AFTER DELETE
AS
BEGIN
    INSERT INTO logs_acesso (usuario, acao, tabela_afetada, registro_id, resultado, detalhes)
    SELECT SYSTEM_USER, 'DELETE', 'clientes', id, 'sucesso', nome
    FROM deleted;
END;
GO

/* =========================
   DADOS DE TESTE
========================= */
INSERT INTO clientes (nome, cpf_cnpj, email, ativo) VALUES
('Empresa A', '11111111111', 'a@email.com', 1),
('Empresa B', '22222222222', 'b@email.com', 1);

INSERT INTO equipamentos (tag, descricao, tipo, instalado_em) VALUES
('TI-101', 'Sensor temperatura', 'sensor', '2023-01-01'),
('FT-202', 'Medidor fluxo', 'medidor', '2023-02-01');

INSERT INTO leituras_sensores (equipamento_id, valor, unidade, qualidade)
VALUES (1, 25.5, '°C', 'bom');

INSERT INTO notas_fiscais (cliente_id, numero_nf, valor_total, emitida_em)
VALUES (1, 'NF001', 1000, GETDATE());
GO