; Arquivo: Pow.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Eleva ao quadrado o valor da RAM[1] e armazena o resultado na RAM[0].
; Só funciona com números positivos
leaw $R1, %A
movw (%A), %D
leaw $R2, %A
movw %D, (%A)
leaw $1, %A
movw %A, %S
leaw $R4, %A
movw %S, (%A)
WHILE:
	;multiplier
	leaw $R2, %A
	addw (%A), %D, %S
	movw %S, (%A)
	;contador
	leaw $R4, %A
	movw (%A), %S
	incw %S
	movw %S, (%A)
	subw %D, (%A), %S
	leaw $WHILE, %A
	jne %S
	nop
leaw $R2, %A
movw (%A), %S
leaw $R0, %A
movw %S, (%A)













