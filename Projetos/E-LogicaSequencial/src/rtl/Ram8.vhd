-- Elementos de Sistemas
-- by Luciano Soares
-- Ram8.vhd

Library ieee; 
use ieee.std_logic_1164.all;
  
entity Ram8 is
	port(
		clock:   in  STD_LOGIC;
		input:   in  STD_LOGIC_VECTOR(15 downto 0);
		load:    in  STD_LOGIC;
		address: in  STD_LOGIC_VECTOR(2 downto 0);
		output:  out STD_LOGIC_VECTOR(15 downto 0)
	);
end entity;

architecture arch of Ram8 is

component Register16 is
	port(
		clock:   in STD_LOGIC;
		input:   in STD_LOGIC_VECTOR(15 downto 0);
		load:    in STD_LOGIC;
		output: out STD_LOGIC_VECTOR(15 downto 0)
	);

end component Register16;

component Mux8Way16 is
	port ( 
			a:   in  STD_LOGIC_VECTOR(15 downto 0);
			b:   in  STD_LOGIC_VECTOR(15 downto 0);
			c:   in  STD_LOGIC_VECTOR(15 downto 0);
			d:   in  STD_LOGIC_VECTOR(15 downto 0);
			e:   in  STD_LOGIC_VECTOR(15 downto 0);
			f:   in  STD_LOGIC_VECTOR(15 downto 0);
			g:   in  STD_LOGIC_VECTOR(15 downto 0);
			h:   in  STD_LOGIC_VECTOR(15 downto 0);
			sel: in  STD_LOGIC_VECTOR(2 downto 0);
			q:   out STD_LOGIC_VECTOR(15 downto 0));

end component Mux8Way16;

component DMux8Way16 is
	port ( 
			a:   in  STD_LOGIC_VECTOR(15 downto 0);
			sel: in  STD_LOGIC_VECTOR(2 downto 0);
			q0:  out STD_LOGIC_VECTOR(15 downto 0);
			q1:  out STD_LOGIC_VECTOR(15 downto 0);
			q2:  out STD_LOGIC_VECTOR(15 downto 0);
			q3:  out STD_LOGIC_VECTOR(15 downto 0);
			q4:  out STD_LOGIC_VECTOR(15 downto 0);
			q5:  out STD_LOGIC_VECTOR(15 downto 0);
			q6:  out STD_LOGIC_VECTOR(15 downto 0);
			q7:  out STD_LOGIC_VECTOR(15 downto 0));
end component DMux8Way16;

signal output_dmux,output_reg:STD_LOGIC_VECTOR(127 downto 0);

begin
	dm : DMux8Way16 port map(input,address,
		output_dmux(127 downto 112),
		output_dmux(111 downto 96),
		output_dmux(95 downto 80),
		output_dmux(79 downto 64),
		output_dmux(63 downto 48),
		output_dmux(47 downto 32),
		output_dmux(31 downto 16),
		output_dmux(15 downto 0));
	

	r1 : Register16 port map(clock,output_dmux(127 downto 112),load,output_reg(127 downto 112));
	r2 : Register16 port map(clock,output_dmux(111 downto 96),load,output_reg(111 downto 96));
	r3 : Register16 port map(clock,output_dmux(95 downto 80),load,output_reg(95 downto 80));
	r4 : Register16 port map(clock,output_dmux(79 downto 64),load,output_reg(79 downto 64));
	r5 : Register16 port map(clock,output_dmux(63 downto 48),load,output_reg(63 downto 48));
	r6 : Register16 port map(clock,output_dmux(47 downto 32),load,output_reg(47 downto 32));
	r7 : Register16 port map(clock,output_dmux(31 downto 16),load,output_reg(31 downto 16));
	r8 : Register16 port map(clock,output_dmux(15 downto 0),load,output_reg(15 downto 0));

	mx : Mux8Way16 port map(
		output_reg(127 downto 112),
		output_reg(111 downto 96),
		output_reg(95 downto 80),
		output_reg(79 downto 64), 
		output_reg(63 downto 48),
		output_reg(47 downto 32),
		output_reg(31 downto 16),
		output_reg(15 downto 0),
		address,output);


end architecture;