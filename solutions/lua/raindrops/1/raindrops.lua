local raindrops_converter = function(n)
  local buffer_table = {}
  if n % 3 == 0 then table.insert(buffer_table, "Pling") end
  if n % 5 == 0 then table.insert(buffer_table, "Plang") end
  if n % 7 == 0 then table.insert(buffer_table, "Plong") end
  if #buffer_table == 0 then table.insert(buffer_table, tostring(n)) end
  return table.concat(buffer_table, "")
end
return raindrops_converter

--i do miss python sometimes..