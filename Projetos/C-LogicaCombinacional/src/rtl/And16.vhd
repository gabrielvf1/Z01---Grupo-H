library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity and16 is
	port ( 
			a:   in  STD_LOGIC_VECTOR(15 downto 0);
			b:   in  STD_LOGIC_VECTOR(15 downto 0);
			q:   out STD_LOGIC_VECTOR(15 downto 0));
end and16;

architecture rtl of and16 is
begin 
	q <= (a and b);
end rtl;
