import{j as n,s as i,r as o,G as l,aC as c,aD as m}from"./index-CS89oW_i.js";const p=({className:s,...a})=>n.jsx("nav",{"aria-label":"pagination",className:i("mx-auto flex w-full justify-center",s),...a});p.displayName="Pagination";const x=o.forwardRef(({className:s,...a},e)=>n.jsx("ul",{ref:e,className:i("flex flex-row items-center gap-1",s),...a}));x.displayName="PaginationContent";const g=o.forwardRef(({className:s,...a},e)=>n.jsx("li",{ref:e,className:i("",s),...a}));g.displayName="PaginationItem";const t=({className:s,isActive:a,size:e="md",...r})=>n.jsx("a",{"aria-current":a?"page":void 0,className:i(l({variant:a?"primary":"ghost",size:e}),s),...r});t.displayName="PaginationLink";const d=({className:s,...a})=>n.jsxs(t,{"aria-label":"Go to previous page",size:"md",className:i("gap-1 pl-2.5",s),...a,children:[n.jsx(c,{className:"h-4 w-4"}),n.jsx("span",{children:"Previous"})]});d.displayName="PaginationPrevious";const N=({className:s,...a})=>n.jsxs(t,{"aria-label":"Go to next page",size:"md",className:i("gap-1 pr-2.5",s),...a,children:[n.jsx("span",{children:"Next"}),n.jsx(m,{className:"h-4 w-4"})]});N.displayName="PaginationNext";export{p as P,d as a,t as b,x as c,g as d,N as e};