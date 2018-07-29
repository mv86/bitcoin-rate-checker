DROP TABLE IF EXISTS bitcoin_price_history;

CREATE TABLE bitcoin_price_history (
	id SERIAL4 PRIMARY KEY NOT NULL,
	bitcoin_idx_rate NUMERIC(9,4) NOT NULL,
	coindesk_rate NUMERIC(9,4) NULL,
	mean_avg NUMERIC(9,4) NOT NULL,
	created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);