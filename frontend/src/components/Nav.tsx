import { NavLink } from "react-router";
import type { IconType } from "react-icons";
import { LuHouse, LuInfo } from "react-icons/lu";

import cn from "../lib/cn";

type NavBarLink = { label: string; to: string; icon: IconType };

const links: NavBarLink[] = [
  { label: "Home", to: "/", icon: LuHouse },
  { label: "About", to: "/about", icon: LuInfo },
];

function Nav() {
  return (
    <nav>
      <ul>
        {links.map((link) => {
          const Icon = link.icon;
          return (
            <li key={link.to}>
              <NavLink
                to={link.to}
                end={link.to === "/"}
                className={({ isActive }) =>
                  cn(
                    "flex items-center gap-3 rounded-lg px-3 py-2 my-2",
                    isActive ? "bg-gray-300" : "hover:bg-gray-200",
                  )
                }
              >
                <Icon className="h-5 w-5" />
                {link.label}
              </NavLink>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}

export default Nav;
