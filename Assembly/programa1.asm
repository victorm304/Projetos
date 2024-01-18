section .data

msg:	db "Salve, simpatia!",10	; 'msg' - rótulo dos dados definidos
					; 'db'  - os dados são definidos como
					;	  uma cadeia de bytes.

len:	equ $ - msg			; len - rótulo do tamanho da mensagem
					; equ - pseudo-instrução para definir constantes
					; $   - endereço do último byte escrito na memória
					; msg - endereço do primeiro byte da mensagem

section .text

	global _start			; A diretiva 'global' torna o rótulo '_start'
					; visível de qualquer parte do programa.

_start:					; Aqui está o início do programa.

	mov	rax,	1		; Chamada de sistema 'sys_write'.
	mov	rdi,	1		; Descritor de arquivos 1 (stdout).
	mov	rsi,	msg		; Ponteiro para a string na memória.
	mov	rdx,	len		; Constante com o tamanho da string.
	syscall				; Invoca a chamda de sistema com os
					; dados nos registradores.

_end:

	mov rax,	60		; Chamada de sistema 'sys_exit'
	mov	rdi,	0		; Retorno 0 (sucesso)
	syscall
