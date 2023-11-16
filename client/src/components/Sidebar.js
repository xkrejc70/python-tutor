// Move styles to index.css
import "./Sidebar.css";
import React, { useState } from "react";
import {
  RiHome4Line,
  RiTeamLine,
  RiCalendar2Line,
  RiFolder2Line,
  RiUserFollowLine,
  RiPlantLine,
  RiStackLine,
  RiUserUnfollowLine
} from "react-icons/ri";
import { FiChevronsLeft, FiChevronsRight } from "react-icons/fi/";
import {
  Sidebar,
  SubMenu,
  Menu,
  MenuItem
  //useProSidebar
} from "react-pro-sidebar";
import { Link, createBrowserRouter } from 'react-router-dom'


function Sidebars() {
  //const { collapseSidebar } = useProSidebar();
  const [collapsed, setCollapsed] = useState(false);

  const [toggled, setToggled] = useState(false);

  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };

  return (
    <div>
      <Sidebar
        className={`app ${toggled ? "toggled" : ""}`}
        style={{ height: "100%", position: "absolute" }}
        collapsed={collapsed}
        toggled={toggled}
        handleToggleSidebar={handleToggleSidebar}
        handleCollapsedChange={handleCollapsedChange}
      >
        <main>
          <Menu>
            {collapsed ? (
              <MenuItem
                icon={<FiChevronsRight />}
                onClick={handleCollapsedChange}
              ></MenuItem>
            ) : (
              <MenuItem
                suffix={<FiChevronsLeft />}
                onClick={handleCollapsedChange}
              >
                <div
                  style={{
                    padding: "9px",
                    // textTransform: "uppercase",
                    fontWeight: "bold",
                    fontSize: 14,
                    letterSpacing: "1px"
                  }}
                >
                  PYTHON TUTOR
                </div>
              </MenuItem>
            )}
            <hr />
          </Menu>

          <Menu>
            <Link to="/evaluation">
              <MenuItem icon={<RiHome4Line />}>
                Vyhodnocení
              </MenuItem>
            </Link>
            <SubMenu defaultOpen label={"Example"} icon={<RiTeamLine />}>
              <MenuItem icon={<RiUserFollowLine />}>Regex</MenuItem>
              <MenuItem icon={<RiUserUnfollowLine />}>List</MenuItem>
              <MenuItem icon={<RiCalendar2Line />}>Set</MenuItem>
            </SubMenu>
          </Menu>
        </main>
      </Sidebar>
    </div>
  );
}
export default Sidebars;
