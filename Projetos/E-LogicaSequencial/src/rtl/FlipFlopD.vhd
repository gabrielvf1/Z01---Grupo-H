-- Elementos de Sistemas
-- by Luciano Soares
-- FlipFlopD.vhd

library ieee;
use ieee.std_logic_1164.all;

entity FlipFlopD is
	port(
		clock:  in std_logic;
		d:      in std_logic;
		clear:  in std_logic;
		preset: in std_logic;
<<<<<<< HEAD
		q:     out std_logic := '0'
=======
		q:     out std_logic
>>>>>>> upstream/master
	);
end entity;

architecture arch of FlipFlopD is
begin
<<<<<<< HEAD
	process(clock,clear,preset) begin
	if(preset='0') and (clear = '1') then
		q <= '0';
	elsif(preset = '1') and (clear = '0')  then
		q <= '1';
	elsif(preset = '1' ) and (clear = '1') then
		q <= '1';
	elsif(rising_edge(clock)) then
		q <= d;
	end if;
end process;
end architecture;
=======


end architecture;
>>>>>>> upstream/master
